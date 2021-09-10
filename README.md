# SPS-2581-Breast-Cancer-Risk-Prediction-using-AWS-SageMaker
Breast Cancer Risk Prediction using AWS SageMaker
https://drive.google.com/file/d/1cS1F5oPabcHW82Gb09a0cRMYL6tAtTzh/view?usp=sharing

# BREAST CANCER PREDICTION USING AMAZON SAGEMAKER

![breast](https://user-images.githubusercontent.com/56153083/132855498-f64c4c56-5959-4f12-8abb-5d41cf67c0e0.jpg)

The purpose of this project is to predict whether the patient has breast cancer or not using machine learning.We acquired the breast cancer dataset from kaggle dataset and used amazon sagemaker’s jupyter notebook for the purpose of coding . The method uses Xgboost classifier and amazon web services like Amazon S3,AWS API Gateway,AWS Lambda,AWS SNS,Amazon SageMaker for completing the project. We will be building and deploying the ml model in aws sagemaker and use sns service to generate email alert about the risk


## Overview

 - [Breast cancer is the second most leading cancer in women compared to all other cancers . Around 1.1 million cases were recorded in 2004. Early diagnostics significantly increases the chances of correct treatment and survival, but this process is tedious and often leads to a disagreement between pathologists. Computer-aided diagnosis systems showed the potential for improving diagnostic accuracy. But early detection and prevention can significantly reduce the chances of death.](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Screening is for all women without symptoms , whether they have a family history of breast cancer or not. Some women choose not to attend for breast screening . Others attend on some occasions . Women's reasons for non attendance vary, some don't go because they feel they are too busy . Also studies suggest that a few women don't go for screening because they are afraid of being diagnosed with breast cancer](https://github.com/matiassingers/awesome-readme)
 - [Considering all these reasons it is very important to detect breast cancer as early as possible](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

![AWS_Learning_Path](https://user-images.githubusercontent.com/56153083/132846864-34650319-6055-4f3a-ae2e-5a5efe27993a.png)


  ## Amazon web service tools used in this project

1) AMAZON SAGEMAKER:
Amazon SageMaker is a fully-managed service that enables data scientists and developers to quickly and easily build, train, and deploy machine learning models at any scale. Amazon SageMaker includes modules that can be used together or independently to build, train, and deploy your machine learning models

2) AMAZON S3
An Amazon S3 bucket is a public cloud storage resource available in Amazon Web Services' (AWS) Simple Storage Service (S3).


3) AWS LAMBDA
 AWS Lambda lets you run code without provisioning or managing servers. You pay only for the computing time you consume. With lambda , you can run code for virtually any type of application or backend service - all with zero administration . Just upload your code and lambda takes care of everything required to run and scale your code with high availability.

4) AWS API GATEWAY
Amazon API Gateway is an AWS service for creating, publishing, maintaining, monitoring,
And securing. REST, HTTP, and WebSocket APIS at any scale.

API Gateway creates RESTful APIs that:
Are HTTP-based and Enable stateless client-server communication.
Implement standard HTTP methods such as GET, POST, PUT, and DELETE


5) AWS SNS SERVICE
Amazon Simple Notification Service (Amazon SNS) is a managed service that provides message delivery from publishers to subscribers (also known as producers and consumers).Clients can subscribe to the SNS topic and receive published messages using a supported protocol, such as Amazon SQS, AWS Lambda, HTTP, email, mobile push notifications, and mobile

![block diagram](https://user-images.githubusercontent.com/56153083/132855472-baa619cd-bbeb-4023-a482-3e4afe828558.png)


  ## Machine learning Algorithm used in the project.
The XGBoost (eXtreme Gradient Boosting) is a popular and efficient open-source implementation of the gradient boosted trees algorithm. Gradient boosting is a supervised learning algorithm that attempts to accurately predict a target variable by combining an ensemble of estimates from a set of simpler and weaker models. The XGBoost algorithm performs well in machine learning competitions because of its robust handling of a variety of data types, relationships, distributions, and the variety of hyperparameters that you can fine-tune. You can use XGBoost for regression, classification (binary and multiclass), and ranking problems.
One can use the new release of the XGBoost algorithm either as a Amazon SageMaker built-in algorithm or as a framework to run training scripts in your local environments.In this project we've used it as a Amazon SageMaker built-in algorithm.
Follow below documentation for more details (https://docs.aws.amazon.com/sagemaker/latest/dg/xgboost.html)


## Documentation

[Refer this Documentation to understand the  project](https://docs.google.com/document/d/1dFuw9yT1zD6mBgq3iu6GBvvZFHpEBGBzQ8i002YcGlg/edit?usp=sharing)

  

























