# ReportReducer
This is a financial tool used for developers that are keen in reading into financial reports when investing, using Ollama Llama 3's open source LLM, it summarizes and highlights key details of the report (PE ratio, Earnings, any key facts etc.) Using a React.js frontend to retreive user files, and a python FLASK backend in order to parse the file, extract the text and prompt the LLM I was able to create the end to end functionality for the application and retreive some key insights into a companies quarterly report.

# Choosing a financial report in order to submit
<img width="1311" alt="image" src="https://github.com/RajanChavada/ReportReducer/assets/77020385/89e6b2fc-055b-4bc0-8de9-565ea14864de">
After choosing the financial report, the user presses on submit making a axios request to the FLASK backend routed here: 
<img width="523" alt="image" src="https://github.com/RajanChavada/ReportReducer/assets/77020385/3658dd55-85b1-4588-b571-678abce4a740">

# Flask backend 
The FLASK backend is responsible for reading the pdf document uploaded, parsing the file and extracting the text in order to use as a prompt for the LLM 
The prompt it given to the LLM and sent back to the front end in order to display the result: 
<img width="1279" alt="image" src="https://github.com/RajanChavada/ReportReducer/assets/77020385/062ba2c5-31f9-4a72-8216-54c4e09c490c">


# Future Alterations to be made: 
- Including a prompt input so users can create custom prompts for the tool
- Including more styling for the output test and application overall
- Improving the speed of the data retreival from LLM possibly
- Including a scraper pre-processor to grab key words from the document using python script to be easier for the LLM





