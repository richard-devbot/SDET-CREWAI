import time
from crewai import Crew
from agents import AutomationAgents
from tasks import WebsiteAutomationTask
import streamlit as st
from crewai import Process
# from dotenv import load_dotenv
# load_dotenv()

agents = AutomationAgents()

css_selector_tester = agents.CSS_Selector_Test_Case_Writer()
gherkin_writer = agents.Gherkin_Feature_File_Writer()
python_automator = agents.Python_Automation_Script_Writer()
qa_reviewer = agents.Quality_Assurance_Reviewer()

tasks = WebsiteAutomationTask()

css_selector_task = tasks.css_selector_test_case_writing(agent=css_selector_tester)
gherkin_task = tasks.gherkin_feature_file_creation(agent=gherkin_writer)
python_automation_task = tasks.python_automation_script_development(agent=python_automator)
qa_review_task = tasks.qa_review_and_integration(agent=qa_reviewer)

# Create lists to store tasks
all_tasks = [css_selector_task, gherkin_task, python_automation_task, qa_review_task]

st.subheader(":green[Revolutionizing Automation Testing with AI!]")
st.sidebar.title(":green[## Designed By Richardson Gunde 🎨]")
st.sidebar.markdown("""
    🚀 Excited to share a breakthrough in Automated Testing with AI! 💻🤖

    Introducing our AI-powered Testing Assistant - your go-to solution for automating the testing process using advanced techniques. 🌟

    With this innovative system, we're streamlining the process of creating CSS selector test cases, writing Gherkin feature files, developing Python automation scripts, and performing comprehensive QA reviews.

    Try it out now and experience the future of automated testing! 💡💼

    ---

    🔗 Simply input the requirements, and watch as our AI-powered system creates:
    - Detailed CSS selector test cases
    - Clear Gherkin feature files
    - Efficient Python automation scripts
    - Comprehensive QA reviews

    ---

    🤝 **Contributions Welcome**

    If you want to contribute to this tool, please let us know. We are open-source developers!

    ---

    🔗 Linkedin : [Richardson Gunde](Linkedin URL)
    📧 Gmail : [gunderichardson@gmail.com](mailto:gunderichardson@gmail.com)
    """)

# Setup Crew
crew = Crew(
    agents=[
        css_selector_tester,
        gherkin_writer,
        python_automator,
        qa_reviewer
    ],
    tasks=all_tasks,
    max_rpm=29,
    verbose=2,
    process=Process.sequential
)

start_time = time.time()

if st.button("Start Process"):
    result = crew.kickoff()
    st.write("Process completed!")
    st.write(result)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Crew kickoff took {elapsed_time} seconds.")
print("Crew usage", crew.usage_metrics)