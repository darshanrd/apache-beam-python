# Dataflow Word Count Tutorial using the Apache Beam Python SDK

To see what code we will be running today, you can visit the Apache Beam GitHub repository's example [wordcount](https://github.com/darshanrd/apache-beam-python/blob/main/dataflow_wordcount.py).

Please follow the below instructions to set up your 

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

Ensure you provide right roles and premissions to GCS bucket wher you would liek to write the output

## Setup Python Environment

[Set up your environment](https://cloud.google.com/dataflow/docs/quickstarts/quickstart-python#set-up-your-environment)

Install virtualenv and activate a Python virtual environment
Install virtualenv version 13.1.0 or above if it is not installed already.

Install pip3 package
```sudo apt-get install python3-pip```

```pip3 install --upgrade virtualenv \
    --user```

Create a Python virtual environment

```python3 -m virtualenv env```

and activate it.

```source env/bin/activate```

Download the samples and the Apache Beam SDK for Python using the pip3 command
In order to write a Python Dataflow job, you will first need to download the SDK from the repository.

When you run this command, pip3 will download and install the appropriate version of the Apache Beam SDK.

pip3 install --quiet \
    apache-beam[gcp]


Instructions to Create Templates in Dataflow ans using DataflowRunner
[Creating and Staging templates](https://cloud.google.com/dataflow/docs/guides/templates/creating-templates#python)

