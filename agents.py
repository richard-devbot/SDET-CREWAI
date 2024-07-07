import os
from crewai import Agent
from langchain_groq import ChatGroq
import streamlit as st
from crewai_tools import SeleniumScrapingTool
from crewai_tools import SerperDevTool
from langchain_community.llms import Ollama
# from langchain_google_genai import GoogleGenerativeAI

st.title("Website Scraping and Testing Automation")

# website_url = st.text_input("Enter Website URL:")

tool2 = SeleniumScrapingTool(website_url='https://www.saucedemo.com/v1/')
os.environ["SERPER_API_KEY"] = "586dd44d3544a918ea21aa60b2a99741bed6f97d"
search_tool = SerperDevTool()

llm1 = ChatGroq(
            api_key="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",
            model= "llama3-70b-8192"  #"mixtral-8x7b-32768"
        )

# llm2 = GoogleGenerativeAI(model="models/gemini-1.5-flash", google_api_key="AIzaSyAPO8LmtX0hfpnsRYARR9hG7l7bXXohD9g")

llm3 = Ollama(model="stable-code:3b-code-q4_0")



class AutomationAgents():
    def CSS_Selector_Test_Case_Writer(self):
        return Agent(
            role="Element Name Test Case Writer",
            goal="""Create comprehensive and robust test cases for all CSS selectors on the website, 
                    ensuring thorough coverage of element interactions, responsiveness, and cross-browser compatibility.""",
            backstory="""You are a seasoned front-end QA specialist with 8+ years of experience in web testing. 
                         Your expertise lies in crafting meticulous test cases that cover every possible scenario 
                         for CSS selectors. You've worked on complex web applications and e-commerce platforms, 
                         and you understand the nuances of responsive design and cross-browser testing.""",
            verbose=True,
            allow_delegation=True,
            llm=llm1,
            tools=[tool2],
            max_iter=10,
            max_rpm=10     
        )
    
    def Gherkin_Feature_File_Writer(self):
        return Agent(
            role="Gherkin Feature File Writer",
            goal="""Transform detailed CSS selector test cases into clear, concise, and comprehensive 
                    Gherkin feature files that align with BDD best practices and facilitate seamless 
                    communication between stakeholders.""",
            backstory="""As a BDD evangelist with 6+ years of experience, you've mastered the art of 
                         writing Gherkin scenarios that bridge the gap between business requirements and 
                         technical implementations. You've trained numerous teams in BDD methodologies and 
                         have a knack for creating feature files that are both human-readable and 
                         automation-friendly.""",
            verbose=True,
            allow_delegation=True,
            llm=llm1,
            # tools=[search_tool],
            max_iter=10,
            max_rpm=10
        )
    
    def Python_Automation_Script_Writer(self):
        return Agent(
            role="Python Automation Script Writer",
            goal="""Develop robust, scalable, and maintainable Python-based web automation scripts that 
                    execute Gherkin scenarios efficiently, handle edge cases gracefully, and provide 
                    detailed reporting.""",
            backstory="""As a skilled Python Automation Script Writer, you are adept at translating 
                         Gherkin feature files into robust and efficient Python web automation scripts 
                         using frameworks like Selenium or Playwright.""",
                        #  With a decade of experience as an SDET, you've automated testing for various 
                        #  web applications using Python, Selenium, and Pytest. You're well-versed in 
                        #  design patterns for test automation, CI/CD integration, and have contributed 
                        #  to open-source testing frameworks. Your scripts are known for their reliability 
                        #  and ability to handle complex test scenarios.
            verbose=True,
            allow_delegation=True,
            llm=llm1,
            # tools=[search_tool],
            max_iter=15,
            max_rpm=10,           
        )
    
    def Quality_Assurance_Reviewer(self):
        return Agent(
           role="Quality Assurance Reviewer",
            goal="""Ensure the overall quality, efficiency, and effectiveness of the entire test 
                    automation suite by reviewing all components and suggesting optimizations.""",
            backstory="""As a QA leader with 15+ years in the industry, you've overseen testing 
                         strategies for Fortune 500 companies. Your expertise spans manual testing, 
                         automation, performance testing, and security testing. You have a keen eye 
                         for identifying gaps in test coverage and suggesting improvements that 
                         significantly enhance the quality and efficiency of testing processes.""",
            verbose=True,
            allow_delegation=True,
            llm=llm1,
            allow_code_execution=True,
            max_iter=10,
            max_rpm=10
        )


  
