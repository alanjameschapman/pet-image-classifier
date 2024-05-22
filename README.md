# Executive Summary
The client is an online veterinary clinic that offers video consultations with veterinarians. The client wants to develop an image classifier that can predict the species of an animal based on an image provided by the animal owner. This will help the consultants to prepare for the consultation and provide better care to the animals.

The dashboard should also display the top 3 species that the animal may belong to, along with images, in the event that the model is unable to predict the species of the animal with 95% certainty. The probability of each species will be provided alongside, to help the consultant determine the animal in-consult.:

# CRISP-DM Workflow
The CRISP-DM (Cross-Industry Standard Process for Data Mining) workflow is a structured approach to planning a data mining project. Each step of the CRISP-DM workflow will be a different epic and be broken down into user stories and tasks:

## Epic 1: Business Understanding
 The client wants:
- To know the species of animal who is scheduled for a video call to discuss the animal's health with their owner.
- To provide their consultants with a summary of key info and conditions that the animal may have based on their animal.
- To know the top 3 species that the animal may belong to (along with images), in the event that the model is unable to predict the species of the animal with 95% certainty. The probability of each species will be provided alongside, to help the consultant determine the animal in-consult.
- A dashboard (as opposed to an API) that can display the results of the image classifier.
- Conventional data analysis will be used to... (fill in the blank)

### Hypothesis and how to validate?
We hypothesize that a Convolutional Neural Network (CNN) can be trained on the dataset of images of animals to accurately predict the species of the animal based on a new and unseen image. We will validate this hypothesis by training a CNN on the dataset and evaluating its performance on a test set of animal images. As agreed with the client, the model should have an accuracy of at least 95% in predicting the species of the animals.

## ML Business Case
- In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 
- The model's inputs are images of animals and the intended outputs are the species of the animals, along with key info and common diseases based on the animal.

## The rationale to map the business requirements to the Data Visualizations and ML tasks
The business requirements of the client are to develop an image classifier that can predict the animal based on an image. To meet this requirement, we will use a Convolutional Neural Network (CNN) to classify the images of animals based on their species. The CNN model will be trained on the dataset of images of animals and evaluated on a test set of images to determine its accuracy in predicting the species of the animals. The results of the image classifier will be displayed on a dashboard, which will provide the client with the species of the animal and common diseases based on the species. The dashboard will also display the top 3 species that the animal may belong to, along with images, in the event that the model is unable to predict the species of the animal with 95% certainty. The probability of each species will be provided alongside, to help the consultant determine the animal in-consult.

## Epic 2: Data Understanding
- The dataset has been taken from Kaggle and is publicly available [here](https://www.kaggle.com/datasets/rafsunahmad/choose-your-pet).
- There are 2262 images split into 74 directories (animals), where each directory has between 27 and 50 images; the median is perhaps 30 images per directory.
- Images are high res (1000-2000px per side). Image file size ranges from 10kB-1MB with the median around 500kB perhaps. NB. GitHub docs suggests limit for GitHub Free plan is actually 2GB so this shouldn't cause a problem.
- There are no Ethical or Privacy concerns regarding the dataset, which does not contain any personal information or sensitive data.

## Epic 3: Data Preparation

## Epic 4: Modeling

## Epic 5: Evaluation

## Epic 6: Deployment
- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
- Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).


# Agile Methodology
The project was managed using Agile methodology, which is an iterative and incremental approach to software development. The project was divided into sprints, with each sprint lasting 2 weeks. The project will be divided into epics, user stories, and tasks, which will be tracked using a project management tool such as Trello or Jira. The Agile methodology will help ensure that the project is delivered on time and meets the client's requirements.


## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


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

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site


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
