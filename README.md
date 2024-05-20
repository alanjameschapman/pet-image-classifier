## Overview
The client is an online veterinary clinic that offers video consultations with veterinarians. The client wants to develop an image classifier that can predict the species of an animal based on an image provided by the animal owner. This will help the consultants to prepare for the consultation and provide better care to the animals. The client wants a dashboard (as opposed to an API) that can display the results of the image classifier, including the species of the animal and common diseases based on the species. The dashboard should also display the top 3 species that the animal may belong to, along with images, in the event that the model is unable to predict the species of the animal with 95% certainty. The probability of each species will be provided alongside, to help the consultant determine the animal in-consult.:


## Dataset Content
- The dataset has been taken from Kaggle and is publicly available [here](https://www.kaggle.com/datasets/rafsunahmad/choose-your-pet).
- There are 2262 images split into 74 directories (animals), where each directory has between 27 and 50 images; the median is perhaps 30 images per directory.
- Images are high res (1000-2000px per side). Image file size ranges from 10kB-1MB with the median around 500kB perhaps. NB. GitHub docs suggests limit for GitHub Free plan is actually 2GB so this shouldn't cause a problem.
- There are no Ethical or Privacy concerns regarding the dataset, which does not contain any personal information or sensitive data.


## Business Requirements
The client is an online veterinary clinic that offers video consultations with veterinarians. The client wants to develop an image classifier that can predict the species of an animal based on an image. The client wants to:
- Know the species of animal who is scheduled for a video call to discuss the animal's health with their owner.
- Provide their consultants with a summary of key info and conditions that the animal may have based on their animal.
- Know the top 3 species that the animal may belong to (along with images), in the event that the model is unable to predict the species of the animal with 95% certainty. The probability of each species will be provided alongside, to help the consultant determine the animal in-consult.
- Conventional data analysis will be used to... (fill in the blank)


## Hypothesis and how to validate?
We hypothesize that a Convolutional Neural Network (CNN) can be trained on the dataset of images of animals to accurately predict the species of the animal based on the image. We will validate this hypothesis by training a CNN on the dataset and evaluating its performance on a test set of images of animals. As agreed with the client, the model should have an accuracy of at least 95% in predicting the species of the animals.


## The rationale to map the business requirements to the Data Visualizations and ML tasks
The business requirements of the client are to develop an image classifier that can predict the animal based on an image. To meet this requirement, we will use a Convolutional Neural Network (CNN) to classify the images of animals based on their species. The CNN model will be trained on the dataset of images of animals and evaluated on a test set of images to determine its accuracy in predicting the species of the animals. The results of the image classifier will be displayed on a dashboard, which will provide the client with the species of the animal and common diseases based on the species. The dashboard will also display the top 3 species that the animal may belong to, along with images, in the event that the model is unable to predict the species of the animal with 95% certainty. The probability of each species will be provided alongside, to help the consultant determine the animal in-consult.


## ML Business Case
* In the previous bullet, you potentially visualized an ML task to answer a business requirement. You should frame the business case using the method we covered in the course 

- The model's inputs are images of animals and the intended outputs are the species of the animals, along with key info and common diseases based on the animal.


## Dashboard Design
- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other item that your dashboard library supports.
- Later, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project you were confident you would use a given plot to display an insight but subsequently you used another plot type).


## Unfixed Bugs
- You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

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
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

* In this section, you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site


## Acknowledgements (optional)
* Thank the people that provided support through this project.


## Project Notes
Consider these alternatives to 'relu' for activation layers: 'elu', 'selu', and 'swish'.

Each step of the CRISP-DM workflow will be a different epic and be broken down into user stories and tasks:
- Epic 1: Business Understanding
    - User Story 1: Understand the business requirements and objectives.
    Acceptance Criteria: The business requirements and objectives should be clearly defined and understood.
        - Task 1: Meet with the client to discuss the business requirements and objectives.
        - Task 2: Document the business requirements and objectives.
    - User Story 2: Define the success criteria for the project.
    Acceptance Criteria: The success criteria should be clearly defined and agreed upon by the client.
        - Task 1: Define the success criteria for the project.
        - Task 2: Review and finalize the success criteria with the client.
- Epic 2: Data Understanding
    - User Story 1: Collect the dataset of images of animals.
    Acceptance Criteria: The dataset should contain images of various species of animals.
        - Task 1: Download the dataset from Kaggle.
        - Task 2: Explore the dataset to understand its structure and contents. Study for average and variability (LO 3.1)
    - User Story 2: Preprocess the images to prepare them for training.
    Acceptance Criteria: The images should be resized and normalized to a standard size.
        - Task 1: Extract relevant features on which to train the model.
        - Task 2: Resize and normalize the images to a standard size (LO 3.1).
- Epic 3: Data Preparation
    - User Story 1: Split the images into training, validation, and test sets.
    Acceptance Criteria: The images should be split into training, validation, and test sets.
        - Task 1: Split the images into training, validation, and test sets.
        - Task 2: Plot the numbers of images in each set (LO 3.1).
    - User Story 2: Train a Convolutional Neural Network (CNN) on the dataset.
    Acceptance Criteria: The CNN model will be trained and evaluated on the training dataset.
        - Task 1: Train the CNN on the training set.
        - Task 2: Evaluate the model's performance on the validation set.
- Epic 4: Modeling
    - User Story 1: Train a Convolutional Neural Network (CNN) on the dataset.
    Acceptance Criteria: The CNN model will be trained and evaluated on the training dataset.
        - Task 1: Split the images into training, validation, and test sets and plot numbers for each (LO 3.1).
        - Task 2: Train the CNN on the training set.
- Epic 5: Evaluation
    - User Story 1: Evaluate the model's performance on the test set.
    Acceptance Criteria: The model should have an accuracy of at least 95% on the test set.
        - Task 1: Evaluate the model's accuracy on the test set.
        - Task 2: Generate a confusion matrix and Scikit Learn report to visualize the model's performance on the training and test sets (LO 5.2).
        - Task 3: Evaluate and indicate the learning curve (loss and accuracy) of the model (LO 5.2) for both training and validation sets.
- Epic 6: Deployment
    - User Story 1: Create a dashboard to display the results of the image classifier.
    Acceptance Criteria: The dashboard should display the results of the image classifier.
        - Task 1: Design the layout of the dashboard, listing the pages and content and how they relate to the business requirements (LO 6.1).
        - Task 2: Implement the image classifier in the dashboard. Include image montage (LO 3.1)
    - User Story 1: Deploy the model to the dashboard.
    Acceptance Criteria: The model should be deployed to the dashboard.
        - Task 1: Deploy the model to Heroku.
        - Task 2: Test the model's performance on the dashboard.
