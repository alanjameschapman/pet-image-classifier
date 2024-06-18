# Executive Summary

The client is an online veterinary clinic that offers video consultations with veterinarians. The client wants to develop an image classifier that can predict the species of an animal based on an image provided by the animal owner. This will help the consultants to prepare for the consultation and provide better care to the animals.

The dashboard should also display the top 3 species that the animal may belong to, along with images, in the event that the model is unable to predict the species of the animal with 95% certainty. The probability of each species will be provided alongside, to help the consultant determine the animal in-consult.

# CRISP-DM Workflow

The CRISP-DM (Cross-Industry Standard Process for Data Mining) workflow is a structured approach to planning a data mining project. Each step of the CRISP-DM workflow will be a different epic and be broken down into user stories and tasks:

## Epic 1: Business Understanding

![business-understanding](/docs/images/business-understanding.png)

The client's business requirements were framed as user stories for the purposes of managing via GitHub projects and mapping to other project tasks (LO2.1, LO2.2). Links are provided to see the tasks, development notes and screenshots for each user story.

| As a consultant I can... | ...so that I can... | Acceptance Criteria | Mapping to data visualizations and ML tasks |
| :- | :- | :- | :- |
| Identify the animal from an uploaded image | Prepare for the consultation. | Model can correctly predict with 95% accuracy. | Issue [#11](https://github.com/alanjameschapman/pet-image-classifier/issues/11) tasks:<ul><li>Provide an image upload widget on deployed pipeline and dashboard.</li><li>Display prediction on dashboard.</li></ul> |
| See a summary of key info, images, and conditions that the animal may have | Better discuss the animal's health with their owner. |  Images and info displayed on dashboard. | Issue [#12](https://github.com/alanjameschapman/pet-image-classifier/issues/12) tasks:<ul><li> Display images and info based on prediction.</li></ul> |
| Identify the top 3 animals that the image may belong to, ranked by probability | Visually identify the animal using conventional data analysis. | Animals displayed on dashboard visually correlate with uploaded image. | Issue [#13](https://github.com/alanjameschapman/pet-image-classifier/issues/13) tasks:<ul><li>Display images and info based on prediction.</li></ul>
| Use a dashboard (not an API) | Identify an animal from an image upload. | Dashboard is intuitive and easily accessible to consultant | Issue [#14](https://github.com/alanjameschapman/pet-image-classifier/issues/14) tasks:<ul><li>Perform and document manual testing.</li><li>Provide dashboard link to client for feedback.</li></ul> |

The 'top 3' requirement will be particularly useful for cross-breeds, such as Labradoodles and Cockapoos. The probability of each species will be provided alongside, to help the consultant determine the animal in-consult. 

### Hypotheses and validation

| Hypothesis | Validation | Result |
| :- | :- | :- |
| The chosen dataset of images of animals is representative of the animals that the consultants will encounter in practice | The dataset will be reviewed to ensure that it contains a diverse range of animals that the consultants may encounter in practice. | Client was satisfied that the dataset was not deficient in any other animal that was commonly seen during consults. |
| A Convolutional Neural Network (CNN) can be trained on the dataset of images of animals to accurately predict the animal based on a new and unseen image | The model can accurately predict the breed of an unseen image. | Two different datasets were trialled for model training. One with ca. 30 images per breed, another with ca. 150 images per breed. The latter performed better, but still required implementation of transfer learning i.e. using a pre-trained base model to produce sufficient results.  |
| The model can predict the species of the animal with 95% accuracy | The model will be evaluated on a test set of images to determine its accuracy in predicting the species of the animals. The results will be displayed on a dashboard. | The best accuracy achieved was around 80%. Whilst this failed to meet the 95% target, it was enough to provide the functionality required by the client of providing the top 3 breeds based on probability. |
| The model can predict the top 3 animals the image may belong to, in the event that the model is unable to predict the species of the animal with 95% certainty | The model will be evaluated on a test set of images to determine its accuracy in predicting the species of the animals. | The model provides the functionality required by the client of providing the top 3 breeds based on probability. |

## Epic 2: Data Understanding

![data-understanding](/docs/images/data-understanding.png)

- The dataset has been taken from Kaggle and is publicly available [here](https://www.kaggle.com/datasets/rafsunahmad/choose-your-pet).
- There are 2262 images split into 74 directories (animals), where each directory has between 27 and 50 images; the median is perhaps 30 images per directory.
- Image size: images are high res (1000-2000px per side).
- File size: Image file size ranges from 10kB-1MB with the median around 500kB perhaps. NB. GitHub docs suggests limit for GitHub Free plan is actually 2GB so this shouldn't cause a problem. The total dataset size is around 1.1GB.
- There are no Ethical or Privacy concerns regarding the dataset, which does not contain any personal information or sensitive data.

The dataset was reviewed with the client to identify if there were any missing animals. The following dog breeds were identified:

- Springer spaniel
- Border collie
- Jack russell terrier
- Pugs.

The client was satisfied that the dataset was not deficient in any other animal that was commonly seen during consults.

Images of the aforementioned dog breeds were added to the dataset.

The dataset was then checked for quantity and quality:

| Quantity | Quality |
| - | - |
| ![Image](https://github.com/alanjameschapman/pet-image-classifier/assets/137620143/8130687d-8f44-4e62-a4ac-b0289b78597c) | ![Image](https://github.com/alanjameschapman/pet-image-classifier/assets/137620143/907070f0-966a-4a80-ac07-a17ded2bb3f6) |

**Quantity**
The majority of animals have between 27 and 30 images, which is anticipated as being enough to train the model. There is some variation either side of this (minimum = 17, maximum = 49), but it is anticipated that any bias can be removed at the next step. If there is difficulty training the model with this dataset, this will be rectified as required.

**Quality**
The minimum resolution across all images is 100 x 100px. Visually, the image appears to be recognisable as a great dane and therefore deemed acceptable:

![Image](https://github.com/alanjameschapman/pet-image-classifier/assets/137620143/80f64801-cc81-4cb1-af3c-2e9bd156e9f5)

The resolution of many of the images will likely be higher than required. Resolution can be reduced at the next step ([#4](https://github.com/alanjameschapman/pet-image-classifier/issues/4)) to improve the efficiency and speed of the ML pipeline.

## Epic 3: Data Preparation

![data-preparation](/docs/images/data-preparation.png)

The dataset was split into training and testing sets. The training set was used to train the model, and the testing set was used to evaluate the model's performance. The model was trained on the training set and then evaluated on the testing set to determine its accuracy.

## Epic 4: Modeling

![modeling](/docs/images/modeling.png)

The model's inputs are images of animals and the intended outputs are the species of the animals, along with key info and common diseases based on the animal.

After trying two different models, the accuracy and loss plots showed that both struggled to converge over 50 epochs, This indicates that the models were not learning from the data and would not be able to make accurate predictions.

| Model | Accuracy | Loss | Comments |
| :- | :-: | :-: | :- |
| v1 (CI Malaria walkthrough) | ![v1-accuracy](/outputs/v1/model_training_acc.png) | ![v1-loss](/outputs/v1/model_training_losses.png) | The accuracy was around x and the loss was around y. |
| v2 (Kaggle [walkthrough](https://www.kaggle.com/code/ahmadjaved097/multiclass-image-classification-using-cnn/notebook)) | ![v2-accuracy](/outputs/v2/model_training_acc.png) | ![v2-loss](/outputs/v2/model_training_losses.png) | The accuracy was around x and the loss was around y. |

This was likely due to the dataset having too few images per animal - only 30 images on average.

The next step would be to try transfer learning, but after another review of available pet datasets, it was agreed with the client that an alternative dataset would be used to see if that improved model performance. The new dataset is from [Kaggle](https://www.kaggle.com/datasets/amandam1/120-dog-breeds-breed-classification) and contains 20,600 images of dog breeds only. This dataset is more suitable for the client's requirements as it contains a better range of dog breeds (120 v 71 directories) and more images per breed (150 vs 30 images).

## Epic 5: Evaluation



## Epic 6: Deployment

### Dashboard Design

#### Page 1 - Project Overview

- Display the project name, description, and purpose.
- Describe the business problem and the solution.
- Provide a link to the dataset.
- Describe the dataset used to train the model.
- Provide a link to the GitHub repository readme.

#### Page 2 - Animal identification

- Provide an image upload widget.
- Display the predicted species of the animal.
- Display the top 3 breeds that the animal may belong to, along with images and probabilities.
- Button to select breed and display key info and common diseases.

#### Page 4 - Hypotheses and Validation

- Display the hypotheses stated above (see epic 2) and how they were validated.
- Display the results of the validation.

#### Page 5 - Model Performance Metrics

- Display the model's performance metrics, including:
    - Learning curves (plots of accuracy and loss)
    - Confusion matrix for a batch size of 32 (not possible to display for the entire dataset of 120 breeds)
- Generalised model performance on test set (table of accuracy and loss).

### Heroku

The App live link is: https://YOUR_APP_NAME.herokuapp.com/ (TBC)

The project was deployed on Heroku using the following steps.
1. Log in to Heroku and create an App
2. Log into Heroku CLI in the IDE workspace terminal using the bash command: heroku login -i and enter credentials.
3. Run the command git init to re-initialise the Git repository
4. Run the command heroku git:remote -a YOUR_APP_NAME to connect the workspace and your Heroku app.
5. Set the app's stack to heroku-20 using the bash command heroku stack:set heroku-20 to provide compatibility with the Python 3.10.9 version used for this project.
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

- [numpy](https://numpy.org/): NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. Here is an example of how NumPy was used in the project:

- [pandas](https://pandas.pydata.org/): Pandas is a fast, powerful, flexible, and easy-to-use open-source data analysis and data manipulation library built on top of the Python programming language. Here is an example of how Pandas was used in the project:

- [scikit-learn](https://scikit-learn.org/stable/): Scikit-learn is a free machine learning library for the Python programming language. It features various classification, regression, and clustering algorithms, including support vector machines, random forests, gradient boosting, k-means, and DBSCAN. Here is an example of how Scikit-learn was used in the project:

- [Matplotlib](https://matplotlib.org/): Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy. Here is an example of how Matplotlib was used in the project:

- [Seaborn](https://seaborn.pydata.org/): Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. Here is an example of how Seaborn was used in the project:

- [OpenCV](https://opencv.org/): OpenCV is an open-source computer vision and machine learning software library. Here is an example of how OpenCV was used in the project:

- [Pillow](https://python-pillow.org/): Pillow is the friendly PIL fork by Alex Clark and Contributors. PIL is the Python Imaging Library by Fredrik Lundh and Contributors. Here is an example of how Pillow was used in the project:

- [plotly](https://plotly.com/): Plotly is a technical computing company headquartered in Montreal, Quebec, that develops online data analytics and visualization tools. Here is an example of how Plotly was used in the project:

- [TensorFlow](https://www.tensorflow.org/): TensorFlow is an open-source deep learning library developed by Google. It allows you to build and train neural networks for machine learning. Here is an example of how TensorFlow was used in the project:

- [Keras](https://keras.io/): Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano. It was developed with a focus on enabling fast experimentation. Here is an example of how Keras was used in the project:


### Other technologies
- [Python](https://www.python.org/) is an interpreted, high-level and general-purpose programming language.
- [Streamlit](https://streamlit.io/): Streamlit is an open-source app framework for Machine Learning and Data Science projects. It allows you to create web apps for your machine learning projects with minimal effort.
- [VS Code](https://code.visualstudio.com/): Visual Studio Code is a source-code editor developed by Microsoft for Windows, Linux, and macOS. It includes support for debugging, embedded Git control, syntax highlighting, intelligent code completion, snippets, and code refactoring.
- [Jupyter Notebook](https://jupyter.org/): Jupyter Notebook is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations, and narrative text.
- [Heroku](https://www.heroku.com/) is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

### TBC
- [Balsamiq](https://balsamiq.com/) is a user interface design tool for creating wireframes.
- [Cascading Style Sheets)](https://www.w3.org/Style/CSS/Overview.en.html) (CSS) is a stylesheet language used to describe the presentation of a document written in HTML or XML.
- [HTML](https://html.spec.whatwg.org/) is the standard markup language for documents designed to be displayed in a web browser.


## Credits 

- In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The following Kaggle notebook provided inspiration for creating a multi-class image classifier: see [here](https://www.kaggle.com/code/ahmadjaved097/multiclass-image-classification-using-cnn/notebook) by Ahmad Javed and [here](https://www.kaggle.com/code/canentay/inceptionv3-pet-classification/notebook) by Caner Tay.

- [file cmp method](https://docs.python.org/3/library/filecmp.html) for comparing files and identifying duplicates.
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- Epic flow diagram guides were taken from the Code Institute's course notes.
- Additional dataset images were downloaded from [Pexels](https://www.pexels.com/).


## Acknowledgements (optional)
- My wife and kids for their patience and understanding.
- My mentor Marcel, for his guidance and support.
- Code Institute Slack community for their support.


## Project Notes
Consider these alternatives to 'relu' for activation layers: 'elu', 'selu', and 'swish'.

# Manual Testing

## User Stories

User Stories were assessed and categorised as either developer or client. These were tracked throughout the project as [GitHub issues](https://github.com/users/alanjameschapman/projects/5). Links are provided to see the development notes and screenshots for each.

| As a user I can... | ...so that I can... | Checked | Issue# |
| :- | :- | :-: | :-: |
| view all posts summarized | browse topics | &check; | [23](https://github.com/alanjameschapman/whiteboard/issues/23) |

## User Input Validation

User inputs were validated for various incorrect inputs throughout the project. Results for the final site are shown below.

| Page | Input | Test | Outcome | Screenshot | Pass |
| :-: | :-: | :-: | :-: | :-: | :-: |
| [register](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/signup/) | username | no username | prompt to fill in field | ![register-nousername](/docs/testing/register-nousername.png) | &check; |

## Responsiveness

The responsiveness to different screen sizes was checked throughout the project. Results for MVP and final site are shown below, the main visual difference being fonts.

| Stage | iPhone 6/7/8 | iPad | Laptop
| :-: | :-: | :-: | :-: |
| MVP | ![mvpiphone678](/docs/testing/response/mvpiphone678.png) | ![mvpiad](/docs/testing/response/mvpipadair.png) | ![MVPMacBookAir](/docs/testing/response/mvpmacbookair.png)


## Browser Compatibility

Browser compatibility was tested throughout the project as shown below. Using this [MDN guide](https://developer.mozilla.org/en-US/docs/Learn/Tools_and_testing/Cross_browser_testing/Introduction) as a reference, the following was testing in each browser:
- Functionality, navigation and hyperlinks
- Responsiveness
- Aesthetics

| Stage | Chrome | Firefox | Safari
| :-: | :-: | :-: | :-: |
| MVP | &check; | &check; | &check; |
| Final | &check; | &check; | &check; |

## Bugs

Bugs were tracked throughout the project as GitHub issues. Links are provided to see the development notes and screenshots for each.

### Resolved

| Issue | Problem | Screenshot | Solution | Screenshot |
| :-: | :-: | :-: | :-: | :-: |
| [#29](https://github.com/alanjameschapman/whiteboard/issues/29) | Edit button not populating comment box for editing | ![#29](/docs/issues/29-1.png) | Javascript amended from "id_body" to "id_content | ![#29](/docs/issues/29-2.png) |


### Unresolved

The only unresolved bug is the password reset not working. This does not affect the website functionality because the admin can reset passwords manually.

| Issue# | Problem | Screenshot | Comment |
| :-: | :-: | :-: | :-: |
[36](https://github.com/alanjameschapman/whiteboard/issues/36) | password reset not working | ![#36](/docs/issues/36-1.png) | This bug and associated [Issue#7](https://github.com/alanjameschapman/whiteboard/issues/7) for password reset moved to backlog for future development. |

## Lighthouse

The WAVE Web Accessibility Evaluation Tool was used throughout the project to check for accessibility issues. Lighthouse was then used to test the performance, accessibility, best practices and SEO of the deployed site. The PWA score not showing is a [known feature](https://stackoverflow.com/questions/60603960/why-lighthouse-pwa-score-is-blank-even-though-the-page-is-audited).

Page | Mobile | Desktop | Comment |
| :-: | :-: | :-: | :-: |
| [register](https://whiteboard-app-742f545f1848.herokuapp.com/accounts/signup/) | ![register-mobile](/docs/testing/lighthouse/register-mobile.png) | ![register-desktop](/docs/testing/lighthouse/register-desktop.png) | None |

## Code Validation

### HTML

[W3C Markup Validation Service](https://validator.w3.org/) was used to validate the HTML. The Django template language cannot be validated by URI using the W3C validator, so the rendered HTML was copied and pasted into the direct input form for each page.

| Page | W3C URL | Screenshot | Notes | Pass |
| :-: | :-: | :-: | :-: | :-: |
| [register](/registration/signup.html) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fwhiteboard-app-742f545f1848.herokuapp.com%2Faccounts%2Fsignup%2F) | ![register](/docs/testing/register.png) | Errors relate to built-in Django form and don't affect UX or functionality. | &check; |


### CSS

CSS was validated by direct input using [jigsaw W3C Validation Service](https://jigsaw.w3.org/css-validator/) and validates as CSS level 3 + SVG:

<p>
    <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!"/>
    </a>
</p>

### JavaScript

[jshint](https://jshint.com/) was used to validate the only custom JavaScript file, [comments.js](/staticfiles/js/comments.js), used to edit, delete and approve comments.

| File | Screenshot | Description | Pass |
| :-: | :-: | :-: | :-: |
| [comments](/staticfiles/js/comments.js) | ![comments.js](/docs/testing/comments-js.png) | One warning about a function 'getCookie' declared in a loop referencing an outer scoped variable. Reviewed but syntax deemed not difficult to understand. | &check; |

### Python

[CI Python Linter](http://pep8online.com/) was used to validate the custom python files. No errors were found.

| File | Screenshot | Pass |
| :-: | :-: | :-: |
| [admin](/edblog/admin.py) | ![admin](/docs/testing/admin.png) | &check; |
