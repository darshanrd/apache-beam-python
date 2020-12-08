from __future__ import absolute_import
import argparse
import logging
import re
import apache_beam as beam
from past.builtins import unicode
from apache_beam.io import ReadFromText
from apache_beam.io import WriteToText
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import SetupOptions

#parse lines into words
class WordExtractingDoFn(beam.DoFn):
  """Parse each line of input text into words."""
  def process(self, element):
    return re.findall(r'[\w\']+', element, re.UNICODE)

def run(argv=None, save_main_session=True):
  """Main entry point; defines and runs the wordcount pipeline."""
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--input',
      dest='input',
      default='/root/dataflow-beam/kinglear_backup.txt',
#	'gs://dataflow-samples/shakespeare/kinglear.txt',
      help='Input file to process.')
  parser.add_argument(
      '--output',
      dest='output',
      required=False,
      help='Output file to write results to.')
  known_args, pipeline_args = parser.parse_known_args(argv)

  # We use the save_main_session option because one or more DoFn's in this
  # workflow rely on global context (e.g., a module imported at module level).
  pipeline_options = PipelineOptions(pipeline_args)
  pipeline_options.view_as(SetupOptions).save_main_session = save_main_session

  # The pipeline will be run on exiting the with block.
  with beam.Pipeline(options=pipeline_options) as p:

    # Read the text file[pattern] into a PCollection.
    lines = p | 'Read File' >> ReadFromText(known_args.input)

    #count of all words
    counts = (
        lines
        | 'Split' >>
        (beam.ParDo(WordExtractingDoFn()).with_output_types(unicode))
        | 'PairWIthOne' >> beam.Map(lambda x: (x, 1))
        | 'GroupAndSum' >> beam.CombinePerKey(sum)
        | 'Count of All Words' >> beam.Map(print)
        )

    #sum of all words
    words = (
         counts 
         | 'GetValues' >> beam.Values()
         | 'SumOfWords' >> beam.CombineGlobally(sum)
         | 'Sum of all words' >> beam.Map(print)
         )
 
    #words with lowest count
    lowest = (
         counts
         | 'KeyValue Lowest Swap' >> beam.KvSwap()
         | 'Group by Lowest' >> beam.GroupByKey()
         | beam.combiners.Top.Smallest(1)
         | 'words with lowest count' >> beam.Map(print)
         )

 
    #words with highest count
    highest = (
         counts
         | 'KeyValue Highest Swap' >> beam.KvSwap()
         | 'Group by Highest' >> beam.GroupByKey()
         |  beam.combiners.Top.Largest(1)
         | 'word with highest count' >> beam.Map(print)
         )
 
    # Format the counts into a PCollection of strings.
    def format_result(word, count):
      return '%s: %d' % (word, count)

    #count_of_words_output = counts | 'Format' >> beam.MapTuple(format_result)
    #sum_of_words_output = words | 'Format' >> beam.MapTuple(format_result)
    #lowest_words_output = lowest | 'Format' >> beam.MapTuple(format_result)
    #highest_words_output = highest | 'Format' >> beam.MapTuple(format_result)

   # Write the output using a "Write" transform that has side effects.
    #count_of_words_output | 'Write count of words' >> WriteToText(known_args.output + 'count')
    #words | 'Write sum' >> WriteToText(known_args.output + 'sum')
    #lowest | 'Write lowest' >> WriteToText(known_args.output + 'lowest')
    #highest | 'Write highest' >> WriteToText(known_args.output + 'highest')

#main entry point
if __name__ == '__main__':
  logging.getLogger().setLevel(logging.INFO)
  run()
