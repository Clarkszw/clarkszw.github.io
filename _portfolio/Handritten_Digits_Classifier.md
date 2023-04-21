---
title: "Building A Handwritten Digits Classifier"
method: "Machine learning"
skill: "Deep Learning"
excerpt: "In this Project, we'll: 1. explore why image classification is a hard task. 2. observe the limitations of traditional machine learning models for image classification. 3. train, test, and improve a few different deep neural networks for image classification"
header:
  image: https://s3.amazonaws.com/dq-content/244/single_image.svg
  teaser: https://s3.amazonaws.com/dq-content/244/single_image.svg
---

## Backgroud

In this Project, we'll:

* explore why image classification is a hard task
* observe the limitations of traditional machine learning models for image classification
* train, test, and improve a few different deep neural networks for image classification

 Deep neural networks have been used to reach state-of-the-art performance on image classification tasks in the last decade. For some image classification tasks, deep neural networks actually perform as well as or slightly better than the human benchmark. We can read about the history of deep neural networks [here](https://arxiv.org/ftp/arxiv/papers/1803/1803.01164.pdf).

 Before the year 2000, institutions like the United States Post Office used handwriting recognition software to read addresses, zip codes, and more. One of their approaches, which consists of pre-processing handwritten images then feeding to a neural network model is detailed in [this paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.852.5499&rep=rep1&type=pdf).

**Why is image classification a hard task?**

Within the field of machine learning and pattern recognition, image classification (especially for handwritten text) is towards the difficult end of the spectrum. There are a few reasons for this.

* First, each image in a training set is high dimensional. Each pixel in an image is a feature and a separate column. This means that a 128 x 128 image has 16384 features.
* Second, images are often downsampled to lower resolutions and transformed to grayscale (no color). This often results in a loss of detail that's available for training and pattern matching.
* Third, the features in an image don't have an obvious linear or nonlinear relationship that can be learned with a model like linear or logistic regression. In grayscale, each pixel is just represented as a brightness value ranging from 0 to 256.

![greyscale example](https://s3.amazonaws.com/dq-content/244/single_image.svg)

**Why is deep learning effective in image classification?**

Deep learning is effective in image classification because of the models' ability to learn hierarchical representations.

![neural network example](https://s3.amazonaws.com/dq-content/244/nn_learns_hierarchy.png)

## Working With Image Data

Scikit-learn contains a number of [datasets](https://scikit-learn.org/stable/datasets.html) pre-loaded with the library, within the namespace of `sklearn.datasets`. The [`load_digits()` function](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html) returns a copy of [the hand-written digits dataset](http://archive.ics.uci.edu/ml/datasets/Optical+Recognition+of+Handwritten+Digits) from UCI.

Because dataframes are a tabular representation of data, each image is represented as a row of pixel values. To visualize an image from the dataframe, we need to reshape the image back to its original dimensions (28 x 28 pixels). To visualize the image, we need to reshape these pixel values back into the 28 by 28 and plot them on a coordinate grid.