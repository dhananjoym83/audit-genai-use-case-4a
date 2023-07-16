#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Note: The openai-python library support for Azure OpenAI is in preview.
import fitz
import textwrap
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://nprd-pr-genaivang-cns-openai-aihat-3.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "accfd7377fce46ec84084b7815d3183b"


# In[2]:


def Pdf2chunks(pdfReader):
  pg = pdfReader.page_count
  text = ""
  for i in range(0,pg):
    text = text + pdfReader.load_page(i).get_text("text")
  #chunks = textwrap.wrap(text, 2000)
  return text


# In[3]:


Pdf_file ="C:\\Users\\sonalisucharita\\use_case_4a\\Input_Document-Call_Transcript.pdf"
pdfReader = fitz.open(Pdf_file)
document_chunks = Pdf2chunks(pdfReader)
#document_chunks = list(filter(None,document_chunks))


# In[4]:


document_chunks


# In[5]:


#response = openai.Completion.create(
 #engine="GPT-35-Turbo-aihat3",
 #prompt="""Write Process Narrative of the below Call Transcript. It should contain one line purpose of the meeting, names of all the participants from Entity (Company) and Audit Firm with their designations, For each process in the Process Narrative give the description of the process in points and also explain its Risk and control in place in points in a sequential manner.For each point mention an appropriate title"""+document_chunks,
 #temperature=0.3,
 #max_tokens=1990,
 #top_p=1,
 #frequency_penalty=1.6,
 #presence_penalty=0,
 #stop=None)


# In[6]:


prompt_list=["Create from the below Call Transcript in Present Tense. \none line purpose of the meeting and Location of the Meeting and \nList of names of all the participants from Entity (Company) and Audit Firm with their designations in bullet points.\n\n","Write Detailed Process Narrative of the below Call Transcript in Present Tense \nFor each process give the Process Description of the process in number points and also explain its Risk and control in place in points in a sequential manner. \nFor each Process Description mention an appropriate title.\n\n"]


# In[7]:


#Write a Detailed Process 


# In[8]:


result=''


# In[9]:


for prompt in prompt_list:
    response = openai.Completion.create(
      engine="GPT-35-Turbo-aihat3",
      prompt=prompt+document_chunks+'\n\n',
      temperature=0,
      max_tokens=2200,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=None)
    output=response['choices'][0]['text'].strip() 
    output = output.replace("<|im_end|>", "")
    result=result+'\n'+'\n'+'\n'+output


# In[10]:


result


# In[11]:


response


# In[12]:


output=response['choices'][0]['text'].strip()


# In[13]:


type(output)


# In[14]:


output


# In[15]:


#output_decoded = output.encode('utf-8').decode('unicode_escape')


# In[16]:


with open('Business Process Narrative FVT1.txt', 'w') as f:

    f.write(result)


# In[17]:


from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def txt_to_pdf(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()

    lines = text.split('\n')

    doc = SimpleDocTemplate(output_file, pagesize=A4, leftMargin=30, rightMargin=30, topMargin=60)
    styles = getSampleStyleSheet()
    story = []

    # Heading
    heading_style = ParagraphStyle("Heading", fontSize=20, alignment=TA_CENTER)
    heading = Paragraph("Business Process Narrative", heading_style)
    story.append(heading)
    story.append(Spacer(1, 24))  # Add some space below the heading

    # Paragraph customization
    font_style = "Helvetica"      # Options: 'Times-Roman', 'Helvetica', 'Courier'.
    font_size = 12
    line_spacing = 15
    content_style = ParagraphStyle("Content", fontSize=font_size, leading=line_spacing, fontName=font_style)

    for line in lines:
        para = Paragraph(line, content_style)
        story.append(para)
        story.append(Spacer(0.5,15))

    doc.build(story)

input_file = "Business Process Narrative FVT1.txt"
output_file = "Business Process Narrative FVT1.pdf"
txt_to_pdf(input_file, output_file)

processed_file=output_file