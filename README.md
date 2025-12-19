## Olympic Data Analysis System
The Olympic Data Analysis System is a comprehensive data analytics application developed using Python, Flask, FastAPI, and Streamlit. It analyzes historical Olympic data to provide meaningful insights into medal distributions, athlete performance, country-wise achievements, and participation trends. The system uses publicly available Kaggle datasets, including athlete_events and noc_regions, and presents interactive visualizations through a user-friendly interface.


## Features
- Interactive sidebar with radio button selection for multiple analysis modes

Medal Tally Analysis:
- Year-wise, country-wise, and overall medal tallies
- Filter options including year-overall, country-year, and year-country views
- Structured tabular representation for clear comparison

Overall Analysis:
- Key statistics such as number of editions, host cities, sports, events, nations, and athletes
- Trend analysis of participating nations, events, and athletes over time
- Heatmap showing number of events per sport across Olympic editions
- Identification of the most successful athletes overall or by selected sport (top 10)

Country-Wise Analysis:
- Medal tally trends for selected countries over the years
- Sport-wise performance heatmaps for each country
- Top 10 athletes list for the selected country

Athlete-Wise Analysis:
- Age distribution by medal type (gold, silver, bronze, overall)
- Age distribution with respect to sports for gold medalists
- Height vs weight analysis (overall and sport-specific)
- Male vs female participation trends with interactive line selection


## Tech Stack
- Python
- Flask and FastAPI (Backend Processing)
- Streamlit (Frontend Visualization)
- Pandas, NumPy
- Matplotlib, Seaborn, Plotly
- Scipy and data preprocessing utilities
- Kaggle Olympic Datasets (athlete_events, noc_regions)


## How It Works
1. Olympic datasets are cleaned, merged, and preprocessed for analysis.
2. Users select analysis type through sidebar controls.
3. Statistical computations and visualizations are generated dynamically.
4. Interactive charts, heatmaps, and tables provide deep analytical insights.


## Conclusion
The Olympic Data Analysis System offers a powerful and intuitive platform for exploring Olympic history through data. By combining robust preprocessing, multiple analytical perspectives, and rich visualizations, the project demonstrates advanced data analysis and visualization capabilities. It serves as a strong example of end-to-end analytics application development using Python-based technologies.


