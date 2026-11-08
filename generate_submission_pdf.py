from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable
)
from reportlab.lib.enums import TA_LEFT

doc = SimpleDocTemplate(
    "ML_Assignment2_Submission.pdf",
    pagesize=A4,
    leftMargin=0.8 * inch,
    rightMargin=0.8 * inch,
    topMargin=0.8 * inch,
    bottomMargin=0.8 * inch,
    title="ML Assignment 2 Submission",
    author="2026ak05552",
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle(
    "CustomTitle",
    parent=styles["Title"],
    fontSize=18,
    spaceAfter=8,
    textColor=colors.HexColor("#1f2937"),
)

meta_style = ParagraphStyle(
    "Meta",
    parent=styles["Normal"],
    fontSize=10,
    leading=14,
    textColor=colors.HexColor("#4b5563"),
    spaceAfter=2,
)

heading_style = ParagraphStyle(
    "CustomHeading",
    parent=styles["Heading2"],
    fontSize=13,
    spaceBefore=16,
    spaceAfter=6,
    textColor=colors.HexColor("#111827"),
)

subheading_style = ParagraphStyle(
    "CustomSubHeading",
    parent=styles["Heading3"],
    fontSize=11,
    spaceBefore=10,
    spaceAfter=4,
    textColor=colors.HexColor("#374151"),
)

body_style = ParagraphStyle(
    "CustomBody",
    parent=styles["Normal"],
    fontSize=10,
    leading=14,
    spaceAfter=6,
    alignment=TA_LEFT,
)

instruction_style = ParagraphStyle(
    "Instruction",
    parent=styles["Normal"],
    fontSize=9,
    leading=12,
    textColor=colors.HexColor("#6b7280"),
    italic=True,
    spaceAfter=8,
)

story = []

# ============ HEADER ============
story.append(Paragraph("Machine Learning Assignment 2 - Submission", title_style))
story.append(Paragraph("M.Tech (AIML) &bull; Machine Learning &bull; Roll No: 2026ak05552", meta_style))
story.append(Paragraph("Submitted for evaluation &mdash; Deadline: 8 November 2026, 23:59 PM", meta_style))
story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=1.2, color=colors.HexColor("#374151")))
story.append(Spacer(1, 12))

# ============ SECTION 1: GITHUB LINK ============
story.append(Paragraph("1. GitHub Repository Link", heading_style))
story.append(Paragraph(
    "https://github.com/2026ak05552-png/ML_Assignment02_2026ak05552",
    body_style
))
story.append(Paragraph(
    "This repository contains the complete source code for the assignment: <b>app.py</b>, "
    "<b>requirements.txt</b>, <b>README.md</b>, <b>test_data.csv</b>, the <b>model/</b> folder with "
    "saved trained pipelines, and the training scripts. All files were developed and committed "
    "through the course of this assignment.",
    body_style
))
story.append(Spacer(1, 8))

# ============ SECTION 2: STREAMLIT APP LINK ============
story.append(Paragraph("2. Live Streamlit App Link", heading_style))
story.append(Paragraph(
    "https://mlassignment02.streamlit.app/",
    body_style
))
story.append(Paragraph(
    "The application is deployed on Streamlit Community Cloud and opens an interactive frontend "
    "where users can upload test data, select a model, and view evaluation metrics without any "
    "retraining taking place on the server.",
    body_style
))
story.append(Spacer(1, 8))

# ============ SECTION 3: BITS VIRTUAL LAB SCREENSHOT ============
story.append(Paragraph("3. Screenshot - BITS Virtual Lab Execution", heading_style))
story.append(Paragraph(
    "<i>[Screenshot to be inserted here: the Streamlit application running on BITS Virtual Lab]</i>",
    instruction_style
))
story.append(Paragraph(
    "This screenshot serves as proof that the assignment was executed on the BITS Virtual Lab "
    "environment, as required for 1 mark.",
    body_style
))
story.append(Spacer(1, 8))

# ============ SECTION 4: README CONTENT ============
story.append(Paragraph("4. README.md Content", heading_style))
story.append(Spacer(1, 4))

story.append(Paragraph("a. Problem Statement", subheading_style))
story.append(Paragraph(
    "The objective of this project is to predict whether a bank customer will subscribe to a "
    "term deposit, framed as a binary classification problem (yes or no). Using customer and "
    "campaign-related attributes, I trained and compared five different classification models and "
    "packaged the results into a Streamlit web application for interactive demonstration.",
    body_style
))

story.append(Paragraph("b. Dataset Description", subheading_style))
story.append(Paragraph(
    "I selected the Bank Marketing dataset from the UCI Machine Learning Repository "
    "(<i>bank-additional-full.csv</i>). It contains 41,188 customer records, which comfortably "
    "exceeds the minimum requirement of 500 instances. After removing the <i>duration</i> column "
    "to prevent target leakage, the dataset retains 19 input features, well above the required "
    "minimum of 12. The target column <i>y</i> indicates subscription status (<i>yes</i> = 1, "
    "<i>no</i> = 0). The data is imbalanced, with roughly 36,548 negative responses and 4,640 "
    "positive responses.",
    body_style
))

story.append(Paragraph("c. GitHub Repository Link", subheading_style))
story.append(Paragraph(
    "https://github.com/2026ak05552-png/ML_Assignment02_2026ak05552",
    body_style
))

story.append(Paragraph("d. Models Used", subheading_style))
story.append(Paragraph(
    "All five models were trained on the identical train/test split and the same preprocessing "
    "pipeline so that the comparison is fair. The models are:<br/>"
    "&bull; Logistic Regression<br/>"
    "&bull; Decision Tree Classifier<br/>"
    "&bull; K-Nearest Neighbors Classifier<br/>"
    "&bull; Naive Bayes Classifier (Gaussian)<br/>"
    "&bull; Support Vector Machine (LinearSVC)<br/>"
    "Each model was saved as a complete scikit-learn pipeline (.joblib) that bundles preprocessing "
    "and classification together, ensuring that the Streamlit app can load them directly without "
    "retraining.",
    body_style
))

story.append(Paragraph("Model Comparison Table", subheading_style))

comparison_data = [
    ["ML Model Name", "Accuracy", "AUC", "Precision", "Recall", "F1", "MCC"],
    ["Logistic Regression", "0.9009", "0.8008", "0.6905", "0.2188", "0.3322", "0.3516"],
    ["Decision Tree", "0.8418", "0.6258", "0.3131", "0.3384", "0.3252", "0.2360"],
    ["KNN", "0.8972", "0.7444", "0.5839", "0.3039", "0.3997", "0.3719"],
    ["Naive Bayes", "0.8049", "0.7755", "0.3172", "0.6347", "0.4230", "0.3490"],
    ["Support Vector Machine", "0.9014", "0.7979", "0.7164", "0.2069", "0.3211", "0.3502"],
]

comp_table = Table(comparison_data, colWidths=[1.55*inch, 0.72*inch, 0.72*inch, 0.82*inch, 0.72*inch, 0.72*inch, 0.72*inch])
comp_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f2937")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8.5),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#9ca3af")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f9fafb")]),
    ("ALIGN", (1, 0), (-1, -1), "CENTER"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(comp_table)
story.append(Spacer(1, 6))

story.append(Paragraph("Observations on Model Performance", subheading_style))
observation_data = [
    ["ML Model Name", "Observation"],
    ["Logistic Regression",
     "Delivers high accuracy (0.9009) and strong precision (0.6905) but low recall (0.2188), "
     "indicating it is conservative in predicting positive cases. Expected given the class imbalance."],
    ["Decision Tree",
     "Shows moderate accuracy (0.8418) but the lowest AUC (0.6258) and MCC (0.2360). Captures "
     "non-linear patterns but prone to overfitting on this imbalanced dataset."],
    ["KNN",
     "Achieves the best balance with the highest MCC (0.3719) and strong F1 (0.3997). Distance-"
     "based performance benefits from standard scaling, but computationally expensive at "
     "prediction time on large datasets."],
    ["Naive Bayes",
     "Posts the highest recall (0.6347), identifying most positive cases, though at the cost of "
     "lower precision (0.3172). Fast training but assumes feature independence."],
    ["Support Vector Machine",
     "Records the highest accuracy (0.9014) and precision (0.7164) but very low recall (0.2069), "
     "making it overly conservative on the minority class. Effective in high-dimensional spaces "
     "but sensitive to class imbalance."],
]

obs_table = Table(observation_data, colWidths=[1.45*inch, 5.0*inch])
obs_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f2937")),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 8.5),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#9ca3af")),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f9fafb")]),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 4),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
]))
story.append(obs_table)
story.append(Spacer(1, 10))

story.append(Paragraph("Overall Winner", subheading_style))
story.append(Paragraph(
    "The winning model is <b>KNN</b>, selected based on the highest Matthews Correlation "
    "Coefficient (MCC = 0.3719). MCC is the most reliable metric for imbalanced classification. "
    "MCC and F1 are prioritized over accuracy because the dataset is heavily skewed toward "
    "<i>no</i> responses (36,548 vs 4,640).",
    body_style
))

story.append(Spacer(1, 12))
story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#9ca3af")))
story.append(Spacer(1, 6))
story.append(Paragraph(
    "<b>Final checks before submission:</b> GitHub repository link is functional &bull; Streamlit "
    "app link loads correctly &bull; Application runs without errors &bull; All four required app "
    "features are implemented &bull; README content is included in this PDF.",
    instruction_style
))

doc.build(story)
print("PDF created: ML_Assignment2_Submission.pdf")
