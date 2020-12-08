# Dataflow Word Count Tutorial using Apache Beam Python SDK

To see what code we will be running today, you can visit the GitHub repository's example [wordcount](https://github.com/darshanrd/apache-beam-python/blob/main/dataflow_wordcount.py).

Please follow the below instructions to set up your GCP Environment

[Quickstart using Python](https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python)

1. GCP Project 
2. Enabling API's 
3. Creating Service Account 
4. Create a GCS Bucket

In case you would like to work with user account , run the below commands and follow the prompts

```
gcloud init
gcloud auth application-default login
```

Ensure you provide right roles and premissions to GCS bucket where you would like to write the output files to. GCS Admin role (roles/storage.objectAdmin) can be granted for the sake of testing purpose only, not to be used in Production

## Setup Python Environment

[Set up your environment](https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python#set-up-your-environment)

Install virtualenv and activate a Python virtual environment
Install virtualenv version 13.1.0 or above if it is not installed already.

Install pip3 package

```
sudo apt-get install python3-pip
```

```
pip3 install --upgrade virtualenv --user
```

Create a Python virtual environment

```
python3 -m virtualenv env
```

and activate it.

```
source env/bin/activate
```

Download the samples and the Apache Beam SDK for Python using the pip3 command
In order to write a Python Dataflow job, you will first need to download the SDK from the repository.

When you run this command, pip3 will download and install the appropriate version of the Apache Beam SDK.

```
pip3 install --quiet \
    apache-beam[gcp]
```

Git clone the wordcount python file
[wordcount](https://github.com/darshanrd/apache-beam-python/blob/main/dataflow_wordcount.py).

```
git clone https://github.com/darshanrd/apache-beam-python.git
cp apache-beam-python/dataflow_wordcount.py env/lib/python3.7/site-packages/apache_beam/examples/
```

Ensure that the file "dataflow_wordcount.py" has been copied into the virtual env directory where standard apache beam examples are present "env/lib/python3.7/site-packages/apache_beam/examples/"

```
cd env/lib/python3.7/site-packages/apache_beam/examples/
```

##Launch your pipeline on the Dataflow Service

Use Python to launch your pipeline on the Cloud Dataflow service. The running pipeline is referred to as a job.

```python3 -m  dataflow_wordcount     --project <pass_project_id>     --runner DataflowRunner     --temp_location     <pass_gcs_bucket_temp_path>     --input     <pass_gcs_bucket_input_path>  --output     <pass_gcs_bucket_output_path>    --job_name <name_of_the_job>     --region <pass_region>

-- project is the GCP project.

-- runner is the specific execution engine to use to run your pipeline. The DataflowRunner uses the Dataflow Service as the execution engine.

-- temp_location is the storage bucket Cloud Dataflow will use for the binaries and other data for running your pipeline. This location can be shared across multiple jobs.

-- input is the bucket used by the WordCount example to process the wordcount file

-- output is the bucket used by the WordCount example to store the job results.

-- job_name is a user-given unique identifier. Only one job may execute with the same name.

-- region specifies a regional endpoint for deploying your Dataflow jobs.
```

Sample Invocation with DirectRunner
```
python3 -m  dataflow_wordcount     --project pso-wmt-sandbox     --runner DirectRunner     --temp_location     gs://darshan-dataflow/temp     --output     gs://darshan-dataflow/results/output     --job_name dataflow-wordcount  --input gs://dataflow-samples/shakespeare/kinglear.txt     --region us-central1
```

Sample Invocation with DataFlowRunner

```
python3 -m  dataflow_wordcount     --project pso-wmt-sandbox     --runner DataflowRunner     --temp_location     gs://dataflow/temp    --input     gs://dataflow-samples/shakespeare/kinglear.txt  --output     gs://dataflow/results/output     --job_name dataflow-wordcount     --region us-central1
```


###Please follow the below link to Create Templates in Dataflow using DataflowRunner

[Creating and Staging templates](https://cloud.google.com/dataflow/docs/guides/templates/creating-templates#python)

