# Travel Guide Chatbot

## Overview

The Travel Guide Chatbot is a Python application built using Streamlit and Google Cloud services that helps users plan their travel and explore destinations. It provides information about notable attractions, local restaurants, travel options, and more. This README will guide you on how to set up and use the chatbot.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Running the Application](#running-the-application)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Getting Started

### Prerequisites

To run this application, you need to have the following installed on your system:

- Python 3.x
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install)
- [Streamlit](https://streamlit.io/)
- Other Python libraries as mentioned in the code (e.g., `requests`, `pandas`, etc.)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/travel-guide-chatbot.git
   ```

2. Set up your Google Cloud credentials:

   - Obtain a JSON key file from your Google Cloud project and save it as `key.json`.
   - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable in your shell to point to the location of this key file.

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/key.json"
   ```

3. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Configuration

You can configure the chatbot by selecting options like language, country, state, city, timing, budget, weather, allergies, and food preferences through the Streamlit interface. Additionally, you can select the language for audio output.

### Running the Application

Run the application using the following command:

```bash
streamlit run your_app_name.py
```

Replace `your_app_name.py` with the name of your Python script containing the code.

Once the application is running, you can interact with the chatbot by asking questions and receiving travel recommendations.

## Features

- Recommendations for notable attractions in a selected city, taking into account various factors.
- Suggestions for local restaurants based on user preferences and budget.
- Weather information for the selected location.
- Language selection for audio output.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Cloud](https://cloud.google.com/)
- [OpenAI GPT-3](https://openai.com/)
- [Unsplash](https://unsplash.com/) for the background image.
