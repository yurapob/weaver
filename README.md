# Weaver 
## Overview
This application allows users to upload PDF documents and ask questions based on the content of all uploaded documents. Leveraging the power of LlamaIndex for efficient document indexing and searching, the application provides accurate answers to user queries, potentially including the specific sections where these answers are found.

![demo](https://github.com/yurapob/weaver/assets/73793102/5916672c-6ab5-4ad9-a001-dc018cee6e3c)

## Features
* PDF Document Upload
Users can upload multiple PDF documents to the application.
* Question Answering
After uploading documents, users can ask questions and receive answers based on the content of the uploaded documents.
* Section Identification
For each answer provided, the application display the section where the answer was found.

## Technology Stack
* Tkinter: Used for creating the graphical user interface (GUI) that allows users to interact with the application.
* LlamaIndex: Utilized for indexing PDF documents and efficiently searching their content to provide answers to user questions.

## Project structure
    .
    ├── weaver_app              # Source code for the project
    │   ├── ... 
    │   ├── ui                 # Folder with ui components
    │   ├── managers           # Folder with necessary classes
    │   ├── weaver.py          # Main file
    │   └── requirements.txt   # Required libraries and dependencies
    │
    ├── README.md              # Project overview and setup instructions
    └── LICENSE                # The license for the project

## Getting Started

### Prerequisites
* Python 3.11 (recomended)
* pip (Python package installer)

### Installation

1. Clone the repository to your local machine:
    ```
    $ git clone https://github.com/yurapob/weaver.git
    ```

2. Navigate to the project directory:
    ```
    $ cd weaver/weaver_app
    ```
    
3. Install the required dependencies:
    ```
    $ pip install -r requirements.txt
    ```
4. Setup your OpenAI API token in .env file
    ```
    OPENAI_API_KEY="YOUR OPENAI API KEY"
    ```
    
### Running the Application

1. Launch the application with the following command:
   
    ```
    $ python weaver.py
    ```
3. The GUI will open, allowing you to upload PDF documents and ask questions.

## Usage
1. Upload PDF Documents
Click the "Upload" button and select the PDF files you wish to upload.
2. Ask Questions
Enter your question in the provided text field and click the "Submit" button.
3. View Answers
The answers and section, will be displayed in ouput field.


## Contributing
Contributions to improve the model or extend the functionality are welcome. Please follow the standard GitHub pull request process to submit your changes for review.

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
