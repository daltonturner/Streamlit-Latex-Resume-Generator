import streamlit as st
from pylatex import Document, Section, Subsection, Command

def generate_header(name, email, github, linkedin):
	return r"""
	\begin{center}
	{\LARGE \textbf{""" + name + r"""}}

	\vspace{0.5em}

	{\Large \textbf{Email:} """ + email + r"""}

	\vspace{0.5em}

	{\Large \textbf{GitHub:} \faGithub """ + github + r"""}

	\vspace{0.5em}

	{\Large \textbf{LinkedIn:} \faLinkedin """ + linkedin + r"""}

	\end{center}
	"""

def generate_education_section(education_list):
	section = r"""
	\section{Education}
	"""
	for education in education_list:
		section += r"""
		\subsection{""" + education["degree"] + r"""}
		""" + education["school"] + r""" \hfill """ + education["dates"] + r"""
		""" + education["description"] + r"""
		"""
	return section

def generate_experience_section(experience_list):
	section = r"""
	\section{Experience}
	"""
	for experience in experience_list:
		section += r"""
		\subsection{""" + experience["position"] + r"""}
		""" + experience["company"] + r""" \hfill """ + experience["dates"] + r"""
		""" + experience["description"] + r"""
		"""
	return section

if 'education_list' not in st.session_state:
	st.session_state.education_list = []

if 'experience_list' not in st.session_state:
	st.session_state.experience_list = []

if 'name' not in st.session_state:
	st.session_state.name = ""

if 'email' not in st.session_state:
	st.session_state.email = ""

if 'github' not in st.session_state:
	st.session_state.github = ""

if 'linkedin' not in st.session_state:
	st.session_state.linkedin = ""

st.title("Resume Generator")

with st.sidebar:
	st.sidebar.title("Add your information")
	st.session_state.name = st.text_input("Name")
	st.session_state.email = st.text_input("Email")
	st.session_state.github = st.text_input("GitHub URL")
	st.session_state.linkedin = st.text_input("LinkedIn URL")

	education, experience = st.columns(2)

	with education:
		with st.form("Education", clear_on_submit=True):
			st.write("Add Education")
			degree = st.text_input("Degree")
			school = st.text_input("School")
			dates = st.text_input("Dates")
			description = st.text_area("Description")

			# Every form must have a submit button.
			submitted = st.form_submit_button("Add")
			if submitted:
				st.session_state.education_list.append({"degree": degree, "school": school, "dates": dates, "description": description})

	with experience:
		with st.form("Experience", clear_on_submit=True):
			st.write("Add Experience")
			position = st.text_input("Position")
			company = st.text_input("Company")
			dates = st.text_input("Dates")
			description = st.text_area("Description")

			# Every form must have a submit button.
			submitted = st.form_submit_button("Add")
			if submitted:
				st.session_state.experience_list.append({"position": position, "company": company, "dates": dates, "description": description})


# LaTeX template for the resume
resume_template = r"""
\documentclass{article}
\usepackage[left=0.5in,right=0.5in,top=0.5in,bottom=0.5in]{geometry}
\usepackage{fontawesome}

\begin{document}

""" + generate_header(
	st.session_state.name, 
	st.session_state.email,
	st.session_state.github, 
	st.session_state.linkedin
	) + """
""" + generate_education_section(st.session_state.education_list) + """
""" + generate_experience_section(st.session_state.experience_list) + """
\end{document}
"""


if st.button("Generate LaTeX"):
	st.code(resume_template, language = "latex")
	st.write("""$resume_template$""")

# if st.button("print experience_list"):
# 	st.write(st.session_state.experience_list)

# if st.button("print education_list"):
# 	st.write(st.session_state.education_list)

# def convert_latex_to_pdf(latex_string):
#     # Create a new document
#     doc = Document()

#     # Add the LaTeX string to the document
#     doc.append(latex_string)

#     # Generate the PDF
#     pdf = doc.generate_pdf()

#     return pdf


# # Create a button to run the conversion function
# if st.button("Convert to PDF"):
# 	pdf = convert_latex_to_pdf(resume_template)
# 	# Display the resulting PDF
# 	if pdf:
# 		st.success("PDF created successfully!")
# 		st.write("Here is your PDF:")
# 		st.write(pdf, unsafe_allow_html=True)






