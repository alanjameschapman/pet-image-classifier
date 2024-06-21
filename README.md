# Executive Summary

![responsive](/docs/images/responsive.png)

The client is an online veterinary clinic that offers video consultations with veterinarians. The client wants to develop an image classification dashboard that can identify the breed of a dog based on an image provided by the owner. This will help the consultants prepare for the consultation and ultimately provide better care for the dogs.

The dashboard should also display the top 3 breeds that the dog might belong to according to model certainty. An intuitive and quantitive probability of each breed will be provided to help the consultant determine the animal in-consult. This will be particularly useful if the dog is mixed breed.

The live link is [here](https://pet-image-classifier-5fbc327c6281.herokuapp.com/).

# CRISP-DM Workflow

The CRISP-DM (Cross-Industry Standard Process for Data Mining) workflow is a structured approach to planning a data mining project. Each step of the CRISP-DM workflow will be a different epic and be broken down into user stories and tasks, as detailed below.

## Epic 1: Business Understanding

![business-understanding](/docs/images/business-understanding.png)

The client's business requirements were framed as user stories for the purposes of managing via GitHub projects and mapping to other project tasks. Links are provided to see the tasks, development notes and screenshots for each user story.

| As a consultant I can... | ...so that I can... | Acceptance Criteria | Mapping to data visualizations and ML tasks |
| :- | :- | :- | :- |
| Identify the animal from an uploaded image | Prepare for the consultation. | Model can correctly predict with 95% accuracy. | Issue [#11](https://github.com/alanjameschapman/pet-image-classifier/issues/11) tasks:<br />- Provide an image upload widget on deployed pipeline and dashboard.<br />- Display prediction on dashboard. |
| See a summary of key info, images, and conditions that the animal may have | Better discuss the animal's health with their owner. |  Images and info displayed on dashboard. | Issue [#12](https://github.com/alanjameschapman/pet-image-classifier/issues/12) tasks:<br />- Display images and info based on prediction. |
| Identify the top 3 breeds that the image may belong to, ranked by probability | Visually identify the animal using conventional data analysis. | Animals displayed on dashboard visually correlate with uploaded image. | Issue [#13](https://github.com/alanjameschapman/pet-image-classifier/issues/13) tasks:<br />- Display images and info based on prediction. |
| Use a dashboard (not an API) | Identify an animal from an image upload. | Dashboard is intuitive and easily accessible to consultant | Issue [#14](https://github.com/alanjameschapman/pet-image-classifier/issues/14) tasks:<br />- Perform and document manual testing.<br />- Provide dashboard link to client for feedback.|

The 'top 3' requirement will be particularly useful for cross-breeds, such as Labradoodles and Cockapoos. The probability of each species will be provided alongside, to help the consultant determine the animal in-consult. 

### Hypotheses and validation

| Hypothesis | Validation | Result |
| :- | :- | :- |
| The chosen dataset of dog images is representative of the breeds that the consultants will encounter in-consult. | The dataset will be reviewed by the client. | The client was satisfied that the dataset was suitable. |
| A Convolutional Neural Network (CNN) can be trained on the dataset to accurately predict the breed based on a new and unseen image. | The model can accurately predict the breed(s) of an unseen image. | Two different datasets were trialled for model training. One with ca. 30 images per breed, another with ca. 150 images. The latter performed better, but still required transfer learning i.e. using a pre-trained base model to produce sufficient results.  |
| The model can predict the breed of dog with 95% accuracy | The model will be evaluated on a test set of images to determine its accuracy in predicting the breed. The results will be displayed on a dashboard. | The best accuracy achieved was around 80%. Whilst this failed to meet the 95% target, it was enough to provide the functionality required by the client of providing the top 3 breeds based on probability. |
| The model can predict the top 3 breeds the image may belong to. | The top 3 breeds are displayed according to model certainty. | The model provides the functionality required by the client of providing the top 3 breeds based on certainty. |

## Epic 2: Data Understanding

![data-understanding](/docs/images/data-understanding.png)

The dataset has been taken from Kaggle and is publicly available [here](https://www.kaggle.com/datasets/amandam1/120-dog-breeds-breed-classification/). There are 20,600 images split into 120 directories (dog breeds), with a total file size of 777MB. This gives around:
- File number per breed: 170 images.
- Image size: 440x390px.
- File size: 37kB.
- There are no Ethical or Privacy concerns regarding the dataset, which does not contain any personal information or sensitive data.

The dataset was reviewed with the client to confirm that there were no missing breeds commonly seen during consults.

The dataset was then checked for quantity and quality:

| Quantity | Quality |
| :-: | :-: |
| ![Quantity per breed](/outputs/v5/images_per_dir.png) | ![Average Image Size](/outputs/v5/av_image_dims.png) |
| The median is around 160 images per breed, with a range of around 100-230 images. Outliers are saved in the `outlier_dirs.pkl` file and can be removed if training bias is identified. | The average image size is 440x390px, with a range of 100-3000px. The smallest image size across all images is 105 x 100px. Visually, the image appears to be recognisable as a Rhodesian Ridgeback, and therefore deemed acceptable. See below. |

![Min Res Image](/outputs/v5/min_res_image.png)

The resolution of many of the images are more than sufficient, but were resized to 224x224 pixels to match the expected inputs of the pre-trained model.

## Epic 3: Data Preparation

![data-preparation](/docs/images/data-preparation.png)

The dataset was first checked for any non-images using the `find_non_images` function. This ensured that any subsequent steps were made to images only.

The image folders were already labelled but suffixed with a 10-digit identification, so this was removed using the `rename_directories` function. 

## Epic 4: Modeling

![modeling](/docs/images/modeling.png)

The dataset was split into training, validation and test sets by the ratios of 75/15/15 respectively, which is a standard ratio.

![num_images_per_set](/outputs/v5/num_images_per_set.png)

### Model Development

After trying two different models (v1 and v2), the accuracy and loss plots showed that both failed to converge over 10 epochs, and fluctuated wildly.

This indicated that the models were not learning from the data and would not be able to make accurate predictions. This was likely due to the dataset having too few images per animal - only 30 images on average.

After another review of available pet datasets, it was agreed with the client that an alternative dataset would be used to see if that improved model performance. The new dataset is from [Kaggle](https://www.kaggle.com/datasets/amandam1/120-dog-breeds-breed-classification) and contains 20,600 images of dog breeds only.

This dataset is more suitable for the client's requirements as it contains a better range of dog breeds (120 v 71 directories) and more images per breed (150 vs 30 images). Subsequent models used this dataset and the results of all learning is shown below with comments.

| Model | Accuracy | Loss | Comments |
| :- | :-: | :-: | :- |
| v1 | ![v1-accuracy](/outputs/v1/model_training_acc.png) | ![v1-loss](/outputs/v1/model_training_losses.png) | Learning curves did not converge, and fluctuated wildly. |
| v2 | ![v2-accuracy](/outputs/v2/model_training_acc.png) | ![v2-loss](/outputs/v2/model_training_losses.png) | Learning curves did not converge, and fluctuated wildly. |
| v5 | ![v5-accuracy](/outputs/v5/learning_curve_acc.png) | ![v5-loss](/outputs/v5/learning_curve_loss.png) | Learning curves converged at around 70% accuracy and a loss of 1.
| v5 tuned | ![v5-accuracy](/outputs/v5/learning_curve_tuned_acc.png) | ![v5-loss](/outputs/v5/learning_curve_tuned_loss.png) | Learning curves converged at around 80% accuracy and a loss of 0.75.

### Architecture

Based on the author's research for multi-class models, it was determined that despite the larger dataset, transfer learning would still be required. This required taking an existing model which was 'pre-trained' on a separate and very large image dataset, which has generically useful features which can be repurposed for the classifier task. Here is the base model:

![base model summary](/docs/images/v5_base_model_summary.png)

Note the required input shape of (224, 224, 3) which is the expected image size in RGB, which our input images should conform to. The classifier model is placed onto this base model to create a 'compound' model.

![v5 model summary](/docs/images/v5_model_summary.png)

Note how the number of non-trainable parameters matches that of the base model which has been frozen for initial training, producing the v5 model.

The v5 model was then fine-tuned by 'unfreezing' the top few layers of the base model so that they could be trained together with the classifier model. The resulting model is v5 tuned which is the final model used for training for this project.

![v5 tuned model summary](/docs/images/v5_model_tuned_summary.png)

### Optimization

- Optimizer: Adam optimisation was used to minimise the learning loss adaptively, then rmsprop was used for the fine-tuning stage.
- Learning rate: 0.0001 was used to train the classifier, but when the top layers of the pre-trained model were unfrozen this was reduced by a factor of 10 to avoid overfitting.
- Dropout: 0.2 was used to minimize overfitting and encourage a generalized model which would perform better on new data.

## Epic 5: Evaluation

![evaluation](/docs/images/evaluation.png)

### Model Prediction

For a model with 120 classes, it isn't helpful to create a confusion matrix, classification report or Receiver Operating Characteristic (ROC) curve, but the generalised performance on the test set is as follows:

![v5_model_tuned_evaluation](/outputs/v5/model_tuned_evaluation.png)

The model has an accuracy and loss of around 83% and 0.75 respectively. An accuracy of 83% tells us that the model is good at predicting on unseen test data. Coupled with the dashboard giving threetop predictions based on accuracy, this value should be ample for our purposes. The loss tells us how farthe predicted values deviate from the actual values and 0.75 can be considered good for classification with 120 classes.

Moreover, due to the fact that the top 3 predictions will be presented on the dashboard, this will help to mitigate against model uncertainty.

## Epic 6: Deployment

![deployment](/docs/images/deployment.png)

### Dashboard Design

To present the model predictions to the client, a Streamlit dashboard is used. The structure and layout will be as follows.

#### Page 1 - Project Overview

- Display the project name, description, and purpose.
- Describe the business requirements.
- Provide a link to the GitHub repository readme.

![Overview](/docs/images/overview.png)

#### Page 2 - Animal identification

- Provide an image upload widget.
- Display the top 3 breeds that the animal may belong to, along with probabilities.
- Button/checkbox to select breed and display key info and common diseases (added to backlog).

![id_upload](/docs/images/id_upload.png)
![predictions](/docs/images/predictions.png)

#### Page 3 - Hypotheses and Validation

- Display the hypotheses stated above (see epic 2) and how they were validated.
- Display the results of the validation.

![hypotheses](/docs/images/hypotheses.png)

#### Page 4 - Model Performance Metrics

- Describe the dataset used to train, validate and test the model.
- Display the model's performance metrics, including:
    - Learning curves (plots of accuracy and loss)
    - Generalised model performance on test set (table of accuracy and loss).

![metrics](/docs/images/num_images_per_dir.png)
![learning_curves](/docs/images/learning_curves.png)
![metrics](/docs/images/generalised_performance.png)

### Future Work

| Issue | Description | User Story | Acceptance Criteria | Tasks |
| - | - | - | - | - |
| [#9](https://github.com/alanjameschapman/pet-image-classifier/issues/9) | Plan monitoring and maintenance of the model. | As a developer I can plan monitoring and maintenance of the model so that I can ensure the business tool retains value to the client. | - Monitoring and maintenance plan is documented.<br />- Business tool retains value to the client. | - Discuss and formulate a plan with the client.<br />- Document the plan with the client.<br />- Report all project findings. |
| [#12](https://github.com/alanjameschapman/pet-image-classifier/issues/12) | See a summary of key info, images and common conditions | As a consultant I can see a summary of key info, images, and conditions that the animal may have so that I can better discuss the animal's health with their owner. | Images and info displayed on dashboard. | - Generate a json file with info per breed.<br />- Display images and info based on prediction. |
| [#15](https://github.com/alanjameschapman/pet-image-classifier/issues/15) | Identify whether the image is a dog or not. | As a user I can be notified if the image is not a dog so that I can get value from the tool. | - Set threshold value(s) for dog breed prediction.<br />- If threshold not met, user notified. |



### Heroku

The App live link is: https://pet-image-classifier-5fbc327c6281.herokuapp.com/

The project was deployed on Heroku using the following steps.
1. Log in to Heroku and create an App
2. Log into Heroku CLI in the IDE workspace terminal using the bash command: heroku login -i and enter credentials.
3. Run the command git init to re-initialise the Git repository
4. Run the command heroku git:remote -a pet-image-classifier to connect the workspace and your Heroku app.
5. Set the app's stack to heroku-20 using the bash command heroku stack:set heroku-20 to provide compatibility with the Python 3.8.18 version used for this project.
6. Use git push heroku main to deploy the application to Heroku.

### Forking the GitHub Project

To create a copy of the GitHub repository to modify and experiment with without affecting the original repository, one can fork the repository:

On the repository page, navigate to the Fork button on the top right corner of the page and click on it to create a copy of the repository which should then appear on your own GitHub account.

### Making a Local Clone

1. On the repository page, click on the Code button.
2. To clone the repository using HTTPS, copy the HTTPS URL.
3. Open the IDE of your choice and change the current working directory to the location where you want the cloned directory to be located.
4. Type git clone and paste the previously copied URL to clone the repository.

# Agile Methodology

The project was managed using Agile methodology, which is an iterative and incremental approach to software development. The project was divided into two sprints to coincide with the interim mentor meeting and final submission date. These dates were defined in GitHub projects as Milestones:

![sprints](/docs/images/sprints.png)

The Minimum Viable Product (MVP) would be presented at the interim mentor meeting, with the final product presented at the final submission date. In keeping with the CRISP-DM worklflow, the project was divided into epics, user stories, and tasks, which were tracked throughout the project as GitHub issues. Links are provided to see the development notes and screenshots for each.

![pbi](/docs/images/pbi.png)

## Main Data Analysis and Machine Learning Libraries

- [numpy](https://numpy.org/): NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
- [pandas](https://pandas.pydata.org/): Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and data manipulation library built on top of the Python programming language.
- [scikit-learn](https://scikit-learn.org/stable/): Scikit-learn is a machine learning library for the Python programming language. It features various classification, regression, and clustering algorithms, including support vector machines, random forests, gradient boosting, k-means, and DBSCAN.
- [Matplotlib](https://matplotlib.org/): Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.
- [Seaborn](https://seaborn.pydata.org/): Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
- [Pillow](https://python-pillow.org/): Python Imaging Library (expansion of PIL) is the de facto image processing package for Python language. It incorporates lightweight image processing tools that aids in editing, creating and saving images.
- [plotly](https://plotly.com/): an open-source library that can be used for data visualization and understanding data simply and easily. Plotly supports various types of plots like line charts, scatter plots, histograms, box plots, etc.
- [TensorFlow](https://www.tensorflow.org/): TensorFlow is an open-source deep learning library developed by Google. It allows you to build and train neural networks for machine learning.
- [Keras](https://keras.io/): Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling fast experimentation.

### Other technologies
- [Python](https://www.python.org/) is an interpreted, high-level and general-purpose programming language.
- [Streamlit](https://streamlit.io/): Streamlit is an open-source app framework for Machine Learning and Data Science projects. It allows you to create web apps for your machine learning projects with minimal effort.
- [VS Code](https://code.visualstudio.com/): Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux, and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring.
- [Jupyter Notebook](https://jupyter.org/): Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.
- [Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

# Manual Testing

## User Input Validation

User inputs were validated for various incorrect inputs throughout the project. Results for the final site are shown below.

| Page | Event | Expected Outcome | Pass |
| :-: | :-: | :-: | :-: |
| Overview | Navigate to page | Page loads without errors. | &check; |
| Identification | Navigate to page | Page loads without errors | &check; |
| Identification | Upload image | Image uploads and user notified | &check; |
| Identification | Top 3 predictions displayed with image and information | Information displays without errors | &check; |
| Hypotheses | Navigate to page | Page loads without errors | &check; |
| Metrics | Navigate to page | Page loads without errors | &check; |

## Responsiveness

The responsiveness to different screen sizes was checked throughout the project. Results for the final site are shown below:

![responsive](/docs/images/responsive.png)

## Browser Compatibility

Browser compatibility was tested throughout the project as shown below. Using this [MDN guide](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Introduction) as a reference, the following was testing in each browser:
- Functionality, navigation and hyperlinks
- Responsiveness
- Aesthetics

| Chrome | Firefox | Safari |
| :-: | :-: | :-: |
| &check; | &check; | &check; |

## Credits and Acknowledgements

### Content 

- I used a Tensorflow tutorial for implementing transfer learning. I modified it from binary to multiclassification. Google colab link [here](https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/images/transfer_learning.ipynb?force_kitty_mode=1&force_corgi_mode=1#scrollTo=PpA8PlpQKygw).
- The following Kaggle notebooks provided inspiration for creating a multi-class image classifier: see [here](https://www.kaggle.com/code/ahmadjaved097/multiclass-image-classification-using-cnn/notebook) by Ahmad Javed and [here](https://www.kaggle.com/code/canentay/inceptionv3-pet-classification/notebook) by Caner Tay.
- Cherry Leave Mildew Detection [repo](https://github.com/oks-erm/ML-mildew-detection/tree/main).

### Media

- CRISP-DM flow diagram guides were taken from the Code Institute's course notes.

### Acknowledgements
- My wife and kids for their patience and understanding.
- My mentor Marcel, for his guidance and support.