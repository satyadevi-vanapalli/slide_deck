# import streamlit as st
# # Define the title of your deck
# st.title('My Interactive Slide Deck')

# # Create a sidebar for slide navigation
# slide_select = st.sidebar.selectbox(
#     "Choose Slide",
#     ("Introduction", "Data Overview", "Analysis", "Conclusion")
# )

# # Use if-else statements or a dictionary mapping to display slides based on selection
# if slide_select == "Introduction":
#     st.header("Introduction")
#     st.write("Welcome to our presentation on Streamlit slide decks.")
#     # Add more content here

# elif slide_select == "Data Overview":
#     st.header("Data Overview")
#     # Display data or charts
#     st.write("Here's an overview of our dataset...")

# elif slide_select == "Analysis":
#     st.header("Analysis")
#     # Analysis content
#     st.write("Detailed analysis goes here...")

# elif slide_select == "Conclusion":
#     st.header("Conclusion")
#     st.write("Summary and conclusions.")
# # Example: Adding an interactive chart in the Analysis section
# if slide_select == "Analysis":
#     st.header("Analysis")
#     number = st.slider("Select number of data points", 1, 100, 50)
#     st.write(f"Showing {number} data points.")
#     # Plot a dynamic chart here based on the selected number of data points


# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# # Title of the slide deck
# st.title('Streamlit Slide Deck Example')

# # Sidebar for navigation
# slide_select = st.sidebar.radio("Navigate Slides", 
#                                 ("Introduction", "Data Overview", "Interactive Analysis", "Conclusion"))

# # Introduction slide
# if slide_select == "Introduction":
#     st.header("Welcome to the Streamlit Slide Deck!")
#     st.write("""
#     In this presentation, we'll explore how to use Streamlit to create an interactive slide deck.
#     From data visualization to interactive analysis, Streamlit makes it easy to share your findings and insights.
#     """)

# # Data Overview slide
# elif slide_select == "Data Overview":
#     st.header("Data Overview")
#     # Generating a random dataset for demonstration
#     data = pd.DataFrame({
#         'x': range(1, 101),
#         'y': np.random.randn(100).cumsum()
#     })
#     st.write("Here's a simple dataset we'll be using for demonstration purposes:")
#     st.dataframe(data.head(10))
#     st.line_chart(data)

# # Interactive Analysis slide
# elif slide_select == "Interactive Analysis":
#     st.header("Interactive Analysis")
    
#     # Interactive widget
#     number_of_data_points = st.slider('Number of data points', min_value=10, max_value=100, value=50)
    
#     # Generate sample data
#     sample_data = pd.DataFrame({
#         'x': range(1, number_of_data_points + 1),
#         'y': np.random.randn(number_of_data_points).cumsum()
#     })
    
#     st.write(f"Displaying {number_of_data_points} data points.")
#     st.line_chart(sample_data)

# # Conclusion slide
# elif slide_select == "Conclusion":
#     st.header("Conclusion")
#     st.write("""
#     This simple example demonstrates the capability of Streamlit to create an interactive presentation or slide deck.
    
#     With Streamlit, you can:
#     - Integrate Python code directly into your slides.
#     - Utilize interactive widgets to engage with the audience.
#     - Dynamically update your presentations based on user input or live data.
    
#     Streamlit opens up a plethora of possibilities for data presentation and interactive storytelling.
#     """)

# # Optional: Add a footer
# st.markdown("---")
# st.text("Streamlit Slide Deck Example by OpenAI's ChatGPT")


# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Function to create a sample dataframe
def create_data(n):
    return pd.DataFrame({
        'Date': pd.date_range(start='1/1/2024', periods=n),
        'Sales': np.random.rand(n).cumsum()
    })

# Slide Deck Title
st.title('Streamlit Slide Deck')

# Sidebar for navigation
slide = st.sidebar.radio("Choose your slide:", ["Overview of Streamlit", "Why Streamlit?", "Use cases where Streamlit excels", "Simple Streamlit App", "Streamlit Components","Building an Interactive Application","Advanced Features","Best Practices","Conclusion"])

# Introduction Slide
if slide == "Overview of Streamlit":
    # st.header("##Streamlit Introduction")
    st.write(f"#### Streamlit Introduction")            # <--- works

    # st.write("""
    #     Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. It is a Python-based library specifically designed for machine learning engineers.

    #     """)
    st.write("""Streamlit is a Python library designed to simplify the process of creating web applications, particularly for data science, machine learning, and other data-centric tasks. Its primary purpose is to enable developers and data scientists to quickly build interactive and intuitive web applications directly from Python scripts, without needing expertise in web development technologies like HTML, CSS, or JavaScript.""")
    st.write("##### Brief explanation of Streamlit's features and capabilities")
    st.write("""Streamlit is a powerful tool that transforms data scripts into shareable web apps with minimal coding effort. Here’s a brief overview of its key features and capabilities:
""")
    st.write("##### 1. Ease of Creation and Sharing")
    l1 = "<span><span style='font-weight:600;'>Simple to Use: </span>Convert Python scripts into interactive web apps using straightforward API calls.<span>"
    l2= "<span><span style='font-weight:600;'>Rapid Prototyping: </span>Quickly build and iterate on data applications, seeing changes in real-time as you update your script.<span>"
    s=''
    for i in [l1,l2]:
        s += '- ' + i + "\n\n"
    st.markdown(s, unsafe_allow_html=True)

    st.write("##### 2. Interactivity Without the Complexity")
    l1 = "<span><span style='font-weight:600;'>Widgets: </span>Easily add interactivity with widgets like buttons, sliders, and dropdowns without a callback mechanism—write Python code as if you were writing a script.<span>"
    l2= "<span><span style='font-weight:600;'>State Management: </span>Streamlit automatically manages the app state, simplifying the creation of complex interactive features.<span>"
    s=''
    for i in [l1,l2]:
        s += '- ' + i + "\n\n"
    st.markdown(s, unsafe_allow_html=True)

    st.write("##### 3. Data Handling and Visualization")
    l1 = "<span><span style='font-weight:600;'>Dynamic Data: </span>Incorporate dynamic data sources or real-time updates with ease.<span>"
    l2= "<span><span style='font-weight:600;'>Visualization Support: </span>Seamlessly integrates with major Python data visualization libraries (e.g., Matplotlib, Plotly, Bokeh), allowing for the inclusion of charts and graphs directly within your apps.<span>"
    s=''
    for i in [l1,l2]:
        s += '- ' + i + "\n\n"
    st.markdown(s, unsafe_allow_html=True)

    st.write("##### 4. Layouts and Theming")
    l1 = "<span><span style='font-weight:600;'>Custom Layouts: </span>Control the layout of your app with columns, expanders, tabs, and sidebars, organizing content in a visually appealing manner.<span>"
    l2= "<span><span style='font-weight:600;'>Theming: </span>Customize the look and feel of your app with themes, or create your own to match your branding.<span>"
    s=''
    for i in [l1,l2]:
        s += '- ' + i + "\n\n"
    st.markdown(s, unsafe_allow_html=True)

    st.write("##### 5. Advanced Features")
    l1 = "<span><span style='font-weight:600;'>Session State: </span>Keep track of user interaction across the app through session state.<span>"
    l2= "<span><span style='font-weight:600;'>Caching: </span>Improve performance of data-intensive apps by caching computations and data loading processes.<span>"
    l3= "<span><span style='font-weight:600;'>Components: </span>Extend functionality with custom components or use community-contributed components for added capabilities.<span>"
    s=''
    for i in [l1,l2,l3]:
        s += '- ' + i + "\n\n"
    st.markdown(s, unsafe_allow_html=True)


    st.write("##### 6. Deployment")
    l1 = "<span><span style='font-weight:600;'>Streamlit Sharing: </span>Deploy apps easily with Streamlit Sharing, allowing others to access your app via a web link.<span>"
    l2= "<span><span style='font-weight:600;'>Compatibility with Containers and Cloud Platforms: </span>Streamlit apps can be containerized (using Docker) and deployed on various cloud platforms (e.g., AWS, Google Cloud, Heroku), providing flexibility in how and where you host your app.<span>"
    s=''
    for i in [l1,l2]:
        s += '- ' + i + "\n\n"
    st.markdown(s, unsafe_allow_html=True)
    st.write("""In summary, Streamlit is designed to make the process of creating, sharing, and deploying data applications as straightforward as possible, enabling professionals to focus on data analysis and model building rather than web development.







""")
# Data Overview Slide
elif slide == "Why Streamlit?":
    st.write("##### Why Streamlit? ")
    st.write("Streamlit offers several compelling reasons why it's a preferred choice for building data apps and prototypes:")
    l1 = "<span><span style='font-weight:600;'>Ease of Use: </span>Streamlit provides a simple and intuitive Python API that allows users to create interactive web apps with minimal coding effort. Its syntax is clean and easy to understand, making it accessible to both beginners and experienced developers.<span>"
    l2= "<span><span style='font-weight:600;'>Interactivity: </span>Streamlit facilitates the creation of highly interactive apps without the need for complex web development frameworks. Users can easily incorporate widgets like sliders, dropdowns, and buttons to add interactivity to their apps, enhancing the user experience and enabling dynamic exploration of data.<span>"
    l3= "<span><span style='font-weight:600;'>Python-Centric: </span>Streamlit is designed to leverage Python's strengths, allowing users to write their entire app in Python. This eliminates the need to learn additional languages or frameworks, streamlining the development process and reducing cognitive overhead.<span>"
    l4= "<span><span style='font-weight:600;'>Seamless Integration: </span>Streamlit seamlessly integrates with popular data science libraries like Pandas, Matplotlib, and Plotly, enabling users to leverage their existing knowledge and skills. This integration makes it easy to incorporate data analysis and visualization into Streamlit apps, enhancing their utility and effectiveness.<span>"
    l5= "<span><span style='font-weight:600;'>Deployment Options: </span>Streamlit offers multiple deployment options, including Streamlit Sharing, Docker containers, and cloud platforms like AWS and Heroku. This flexibility allows users to deploy their apps easily and share them with others, ensuring wider accessibility and impact.<span>"
    s=''
    for i in [l1,l2,l3,l4,l5]:
        s += '- ' + i + "\n\n"
    st.markdown(s, unsafe_allow_html=True)
    st.write("""Overall, Streamlit's simplicity, rapid development cycle, interactivity, integration with data science libraries, Pythonic approach, and deployment options make it an attractive choice for building data-driven web applications.""")

    

elif slide == "Use cases where Streamlit excels":
    st.write("##### Use cases where Streamlit excels. ")
    st.write("""Streamlit excels in various use cases where developers need to quickly create interactive web applications for data analysis, machine learning, and visualization. Some of the key use cases where Streamlit shines include:""")

    l1= "<span><span style='font-weight:600;'>Data Exploration and Analysis: </span>Streamlit is ideal for building applications that allow users to explore and analyze datasets interactively. Developers can create intuitive interfaces with interactive widgets and visualizations, enabling users to gain insights from data more effectively.<span>"
    l2= "<span><span style='font-weight:600;'>Machine Learning Prototyping: </span>Streamlit facilitates the rapid prototyping of machine learning models and algorithms. Developers can build interactive applications to showcase model performance, visualize results, and experiment with different parameters, all within a single Python script.<span>"
    l3= "<span><span style='font-weight:600;'>Dashboarding and Reporting: </span>Streamlit is well-suited for creating dashboards and reporting tools that present key metrics, trends, and insights from data in an interactive manner. Developers can integrate various data visualization libraries to create dynamic and visually appealing dashboards for stakeholders.<span>"
    l4= "<span><span style='font-weight:600;'>Education and Training: </span>Streamlit can be used to develop interactive educational tools and tutorials for teaching data science concepts, machine learning algorithms, and programming techniques. Developers can create engaging learning experiences with interactive code snippets, visualizations, and explanations.<span>"
    l5= "<span><span style='font-weight:600;'>Proof of Concepts (POCs): </span>Streamlit is often used to build proof-of-concept applications to demonstrate the feasibility and potential of new data science projects or ideas. Developers can quickly iterate on POCs, gather feedback, and make improvements before investing more time and resources into full-scale development.<span>"
    l6= "<span><span style='font-weight:600;'>Data Visualization and Storytelling: </span>Streamlit enables developers to create compelling data visualizations and storytelling applications that communicate insights and narratives from data. By combining interactive charts, graphs, and text, developers can create engaging experiences for sharing data-driven stories with audiences.<span>"
    l7= "<span><span style='font-weight:600;'>Model Deployment and Monitoring: </span>Streamlit can be used for deploying machine learning models and monitoring their performance in real-time. Developers can create web-based interfaces for deploying models into production environments, enabling users to interact with the models and monitor their behavior.<span>"
    l8= "<span><span style='font-weight:600;'>Collaborative Data Analysis: </span>Streamlit facilitates collaborative data analysis by allowing multiple users to interact with the same application simultaneously. Developers can build shared workspaces where users can collaborate, analyze data together, and share insights in real-time.<span>"
    s=''
    for i in [l1,l2,l3,l4,l5,l6,l7,l8]:
        s += '- ' + i + "\n\n"
    st.markdown(s, unsafe_allow_html=True)

elif slide == "Simple Streamlit App":
    st.write("Here’s a guide on how to create a simple Streamlit App")
    st.write("##### Step 1: Set Up Your Streamlit Environment")
    st.write("First, ensure you have Python and Streamlit installed. If you haven't installed Streamlit yet, you can do so by running:")
    st.code("pip install streamlit")
    st.write("##### Step 2: Create a Python Script")
    st.write("Create a new Python script (e.g., example.py) where you'll define the streamlit code.")
    st.write("##### Step 3: Import Streamlit")
    st.code("import streamlit as st")
    st.write("##### Code:")
    st.code("""import streamlit as st

def main():
    st.title("Simple Streamlit App")
    st.write("Hello, Streamlit!")

if __name__ == "__main__":
    main()
 """)
    st.write("##### Output:")
    # st.image('app.png')
    import streamlit as st
    st.title("Simple Streamlit App")
    st.write("Hello, Streamlit!")
elif slide == "Streamlit Components":
    st.write(f"#### Introduction to Streamlit's core components")    
    st.write("""Streamlit's core components provide the building blocks for creating interactive web applications with Python. Here's an introduction to these core components:""")
    
    l1= "<span><span style='font-weight:600;'>Text: </span>Streamlit allows you to display text using various formatting options such as markdown, HTML, and LaTeX. This component is essential for providing context, instructions, and explanations within your application.<span>"
    l2= "<span><span style='font-weight:600;'>Widgets: </span>Streamlit provides a wide range of widgets that enable user interaction. These include sliders, dropdowns, buttons, checkboxes, and text input fields. Widgets allow users to input data, select options, or trigger actions within the application.<span>"
    l3= "<span><span style='font-weight:600;'>Charts and Plots: </span>Streamlit seamlessly integrates with popular data visualization libraries like Matplotlib, Plotly, and Altair. This allows you to create interactive charts, plots, and graphs to visualize data and present insights to users.<span>"
    l4= "<span><span style='font-weight:600;'>Data Display: </span>Streamlit offers components for displaying data in tabular format. You can easily render Pandas DataFrames, CSV files, or other structured data, enabling users to explore datasets and view information in a structured format..<span>"
    l5= "<span><span style='font-weight:600;'>File Uploader: </span>The file uploader component allows users to upload files directly to the Streamlit application. This is useful for enabling users to input their own data files or upload images, videos, and other media for analysis or processing.<span>"
    l6= "<span><span style='font-weight:600;'>Session State: </span>Streamlit's session state component allows you to persist data across multiple user sessions. This is useful for storing user preferences, settings, or data selections between interactions with the application.<span>"
    l7= "<span><span style='font-weight:600;'>Caching: </span>Streamlit provides caching functionality to optimize the performance of your application. You can use caching to store the results of expensive computations or data loading processes, ensuring that they are only computed once and reused across sessions.<span>"
    l8= "<span><span style='font-weight:600;'>Custom Components: </span>Streamlit allows you to create custom components to extend the functionality of your applications. You can develop custom widgets, visualizations, or interactive elements tailored to your specific requirements, further enhancing the capabilities of your Streamlit apps.<span>"

    s = ''

    for i in [l1,l2,l3,l4,l5,l6,l7,l8]:
        s += '- ' + i + "\n\n"

    st.markdown(s, unsafe_allow_html=True)
    st.write("##### Example:")
    st.code("""import streamlit as st

option = st.selectbox(
   "How would you like to be contacted?",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select contact method...",
)

st.write('You selected:', option)""")
    import streamlit as st

    option = st.selectbox(
   "How would you like to be contacted?",
   ("Email", "Home phone", "Mobile phone"),
   index=None,
   placeholder="Select contact method...",
)

    st.write('You selected:', option)
elif slide == "Building an Interactive Application":
    st.write("##### Demonstration of building a simple interactive application using Streamlit.")
    st.write("""Below is a demonstration of building a simple interactive application using Streamlit. In this example, we'll create a basic calculator that performs addition, subtraction, multiplication, and division based on user input.""")
    st.code("""import streamlit as st

    # Title
    st.title('Simple Calculator')

    # Sidebar for user input
    num1 = st.number_input('Enter first number:')
    num2 = st.number_input('Enter second number:')
    operation = st.radio('Select operation:', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

    # Perform calculation based on selected operation
    if operation == 'Addition':
        result = num1 + num2
    elif operation == 'Subtraction':
        result = num1 - num2
    elif operation == 'Multiplication':
        result = num1 * num2
    elif operation == 'Division':
        if num2 != 0:  # Check for division by zero
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    # Display result
    st.write(f'Result of {operation}: {result}')""")
    import streamlit as st

    # Title
    st.title('Simple Calculator')

    # Sidebar for user input
    num1 = st.number_input('Enter first number:')
    num2 = st.number_input('Enter second number:')
    operation = st.radio('Select operation:', ['Addition', 'Subtraction', 'Multiplication', 'Division'])

    # Perform calculation based on selected operation
    if operation == 'Addition':
        result = num1 + num2
    elif operation == 'Subtraction':
        result = num1 - num2
    elif operation == 'Multiplication':
        result = num1 * num2
    elif operation == 'Division':
        if num2 != 0:  # Check for division by zero
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    # Display result
    st.write(f'Result of {operation}: {result}')
    st.write("To run this Streamlit application, save the code to a file (e.g., calculator.py) and execute it using Streamlit:")
    st.code("streamlit run calculator.py")
    # st.write("This will launch the Streamlit application in your web browser. You can then input two numbers and select an operation from the sidebar to perform the calculation. The result will be displayed below the input fields.")
    st.write("This example demonstrates how quickly and easily you can create interactive applications with Streamlit, allowing users to perform calculations without writing complex HTML, CSS, or JavaScript code.")
elif slide == "Advanced Features":
    st.write("##### Advanced Features of streamlit")
    st.write("""Streamlit offers several advanced features that enhance the functionality and customization of your applications. Here's an overview of some of these advanced features:

""")
    l1= "<span><span style='font-weight:600;'>Custom Components: </span>Streamlit allows you to create custom components to extend the functionality of your applications. Custom components can be built using Python, HTML, CSS, and JavaScript, and integrated seamlessly into your Streamlit apps.<span>"
    l2= "<span><span style='font-weight:600;'>Caching: </span>Streamlit provides caching functionality to optimize the performance of your applications. You can use caching to store the results of expensive computations or data loading processes, ensuring that they are only computed once and reused across sessions.<span>"
    l3= "<span><span style='font-weight:600;'>Session State: </span>Streamlit's session state feature allows you to persist data across multiple user sessions. This is useful for storing user preferences, settings, or data selections between interactions with the application.<span>"
    l4= "<span><span style='font-weight:600;'>Theming: </span>Streamlit allows you to customize the appearance of your applications using themes. You can choose from pre-defined themes or create your own custom themes using CSS, enabling you to match the look and feel of your application to your brand or design preferences.<span>"
    l5= "<span><span style='font-weight:600;'>Sharing and Deployment: </span>Streamlit offers multiple deployment options, including Streamlit Sharing, Docker containers, and cloud platforms like AWS and Heroku. This allows you to deploy your applications easily and share them with others, ensuring wider accessibility and impact.<span>"
    l6= "<span><span style='font-weight:600;'>Security: </span>Streamlit provides features for securing your applications, such as password protection and authentication mechanisms. This allows you to restrict access to sensitive data or functionality within your applications.<span>"
    l7= "<span><span style='font-weight:600;'>Collaboration: </span>Streamlit supports collaboration features that enable multiple users to interact with the same application simultaneously. This is useful for collaborative data analysis, team projects, or shared workspaces where users can collaborate, analyze data together, and share insights in real-time.<span>"
    l8= "<span><span style='font-weight:600;'>Version Control: </span>Streamlit integrates seamlessly with version control systems like Git, enabling you to track changes to your application code and collaborate with team members effectively.<span>"

    s = ''

    for i in [l1,l2,l3,l4,l5,l6,l7,l8]:
        s += '- ' + i + "\n\n"

    st.markdown(s, unsafe_allow_html=True)
    st.write("""These advanced features empower you to build sophisticated and highly customizable applications with Streamlit, tailored to your specific requirements and use cases. Whether you're building data visualization tools, machine learning models, dashboards, or interactive reports, Streamlit provides the flexibility and functionality you need to bring your ideas to life.




""")
elif slide == "Best Practices":
    st.write("##### Tips for building effective Streamlit applications:")
    st.write("""Building effective Streamlit applications involves a combination of best practices, design principles, and optimization techniques. Here are some tips to help you create successful Streamlit applications:

""")
    l1= "<span><span style='font-weight:600;'>Keep it Simple: </span>Streamlit's strength lies in its simplicity. Focus on creating straightforward and intuitive user interfaces that are easy to understand and navigate. Avoid cluttering the interface with unnecessary elements or complex features.<span>"
    l2= "<span><span style='font-weight:600;'>Plan Your Layout: </span>Plan the layout of your application carefully to ensure a logical flow of information and interaction. Use Streamlit's layout components like columns, expanders, and tabs to organize content effectively and optimize screen real estate.<span>"
    l3= "<span><span style='font-weight:600;'>Prioritize Performance: </span>Optimize your code for performance to ensure smooth and responsive user experience. Use caching to store the results of expensive computations or data loading processes and minimize unnecessary computations.<span>"
    l4= "<span><span style='font-weight:600;'>Provide Feedback: </span>Keep users informed about the status of their actions and provide feedback when performing operations or loading data. Use loading spinners, progress bars, or status messages to indicate when tasks are in progress.<span>"
    l5= "<span><span style='font-weight:600;'>Handle Errors Gracefully: </span>Anticipate and handle errors gracefully to prevent crashes or unexpected behavior. Use try-except blocks to catch exceptions and display informative error messages to users.<span>"
    l6= "<span><span style='font-weight:600;'>Include Help and Documentation: </span>Provide help and documentation within your application to guide users on how to use its features and functionalities. Include tooltips, explanatory text, or links to external documentation where necessary.<span>"
    l7= "<span><span style='font-weight:600;'>Test Across Devices and Browsers: </span>Test your application across different devices, screen sizes, and web browsers to ensure compatibility and responsiveness. Streamlit applications are web-based and should adapt well to various viewing environments.<span>"
    l8= "<span><span style='font-weight:600;'>Iterate and Gather Feedback: </span>Continuously iterate on your application based on user feedback and testing. Solicit feedback from users, colleagues, or stakeholders to identify areas for improvement and refine the user experience accordingly.<span>"
    l9= "<span><span style='font-weight:600;'>Document Your Code: </span>Document your code thoroughly to make it easy for others (including your future self) to understand and maintain. Use comments, docstrings, and markdown cells within your Streamlit script to provide context and explanations.<span>"
    l10= "<span><span style='font-weight:600;'>Stay Updated: </span>Stay informed about new features, updates, and best practices in Streamlit by following the official documentation, community forums, and blog posts. Streamlit is actively developed, and new features are regularly introduced to enhance its capabilities.<span>"

    s = ''

    for i in [l1,l2,l3,l4,l5,l6,l7,l8]:
        s += '- ' + i + "\n\n"

    st.markdown(s, unsafe_allow_html=True)
    st.write("""By following these tips, you can build effective and user-friendly Streamlit applications that effectively communicate data insights, facilitate collaboration, and empower users to make informed decisions.





""")
elif slide == "Conclusion":
    st.write("Overall, Streamlit empowers developers, data scientists, and machine learning practitioners to create powerful and engaging web applications for data analysis, visualization, and machine learning. Whether you're building internal tools, dashboards, or interactive demos, Streamlit provides the tools and capabilities you need to bring your ideas to life.")
elif slide == "Data Overview":
    st.header("Data Overview")
    # Display some data
    st.write("Let's look at an example dataset of sales over time.")
    data = create_data(10)  # Create a sample dataset
    st.dataframe(data)  # Display the dataset as a table
    
    # Simple line chart
    st.line_chart(data.set_index('Date'))

# Interactive Analysis Slide
elif slide == "Interactive Analysis":
    st.header("Interactive Analysis")
    st.write("This slide demonstrates how we can make our presentation interactive.")
    
    # Slider for user input
    n_points = st.slider('Select number of data points:', 10, 100, 20)
    dynamic_data = create_data(n_points)
    
    # Plotting the dynamic dataset based on user input
    st.line_chart(dynamic_data.set_index('Date'))
    
    # Show raw data on user request
    if st.checkbox('Show raw data'):
        st.write(dynamic_data)

# Conclusion Slide
elif slide == "Conclusion":
    st.header("Conclusion")
    st.write("""
        Through this presentation, we've seen how Streamlit can be leveraged to create dynamic and interactive slide decks.
        Streamlit's ability to integrate Python code, visualizations, and user interactions makes it an excellent tool
        for data storytelling and presentations.
        
        Thank you for your attention!
        """)

# Optional: Adding a footer for aesthetics
st.markdown("---")
st.markdown("Streamlit Slide Deck Example created by Satyadevi vanapalli")
