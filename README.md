GlobeTrek AI  
Smart Cult Tourism Recommendation Site.  
GlobeTrek AI An AI-based travel app that curates you into great places, creates the best itineraries, chats with an AI travel companion, and esports your trip into a mini-movie with automated recap videos.  
The system combines machine learning, vectors search, natural language processing, recommendation engines, and multimedia creation to provide a smart method of planning travels.  
The site was created in Python, Streamlit, transformer models, FAISS vector search, and Google Gemini AI.  

Key Features  
 In this technology, the robot suggests the destination place the user would visit to obtain certain services or other companies nearby.<|human|>AI Destination Recommendation.  
Recommends cultural spots that are matched with use of semantic search and passing through of the vector embeddings accordingly.  
 Smart Itinerary Generation  
Our travel planner will automatically generate structured multi-day travel plans, depending on the places you are interested in.  
 AI Travel Assistant  
An engaging chat AI provided by Google Gemini API that assists with planning trips and resolving traveling related questions.  
 Travel Video Recap Generator.  
Produces an automated travelling slide show video with the destinations of your itinerary using multimedia tools.  
 PDF Travel Plan Export  
 Asociates you with a cool PDF of the itinerary.  
 Feedback Learning System  
Gathers user feedback and gives analytics, such as:  
	average rating  
	most liked destinations  
	user interest trends  
 Cloud Deployment  
On streamlit Cloud in full operation.  

System Architecture  
The backend is based on a modular AI pipeline that transforms travel queries left by users into intelligent recommendations.  

User Input  

Query Processing  

Embedding Generation  

Vector Similarity Search  

Destination Recommendation  

Region Optimization  

Itinerary Generation  

Travel Video + PDF Export  

User Feedback Learning  
Networks are carried out at different run phases using different modules.  

Mathematical & AI Concepts  
Vector Embeddings  
Transformer models attain the status of natural language queries into high-dimensional vectors.  
Model used:  
SentenceTransformer("all-MiniLM-L6-v2")  
Example transformation:  
Input:  
"historic temples in japan"  

Output vector:  
[0.23, -0.41, 0.18, 0.72, ...]  
These embeddings are not only the keywords and these embeddings reflect the real meaning of the user.  

Cosine Similarity  
Cosine similarity is used to calculate cross-matching between vectors to align user queries to destinations.  
Formula:  
Similarity(A,B)=(A[?]B)/([?][?]A[?][?]x[?][?]B[?][?])  

Where:  
	A = user query vector  
	B = destination vector  

Interpretation:  
Score	Meaning  
1.0	Perfect match  
0.7+	Strong similarity  
0	No relation  
This allows the system to suggest the spots that actually match the query.  

The Vector Search Optimization (FAISS)  
The system relies on FAISS (Facebook AI Similarity Search) to conduct search in haste.  
FAISS constructs a collection of vectors in form of an index and performs nearest neighbor realignment searches.  
Workflow:  
Destination descriptions  

Embedding vectors  

FAISS vector index  

Fast similarity search  
This is to say that a recommendation appears in a flash.  

Backend Modules  
backend The backend is located in the src/ directory.  

Data Processing  
File: src/dataprocessing.py  
Libraries used:  
pandas  
numpy  

Responsibilities:  
	load tourism dataset  
	clean missing values  
	combine text features  
	fasten data ready to embark into creation.  
Example:  
df2["combinedfeatures"], is investigating Site Name + " " + Type" Overall, the updated value that is one of the learning features is the sum of these two components, appearing as a concatenated function.  

AI Embedding Model  
File: src/embeddingmodel.py  
Library used:  
sentence-transformers  

Purpose:  
extract text description and generate vectors to be used as similarity lookups.  

Destination Recommendation Engine.  
File: src/recommenderengine.py  
Libraries used:  
scikit-learn  
faiss  

Steps:  
	Transform user query to embeddings.  
	Similarity Calculate similarity with destination vectors.  
	Rank destinations within score of similarity.  
	Return top recommendations  
Example:  
cosinesimilarity(userembedding, destinationembeddings)  

Location Optimization  
File: src/locationoptimizer.py  
Goal:  
See that the top picks are not at different geographic areas.  

Algorithm:  
Record the frequency of each of the countries.  
Select the country which is the most visible.  
Only results in to that country are filtered.  
Example:  
countrycounts = results [country] valuecounts ()  
bestcountry = countrycounts.pyxmaxunaxudexresult.maximum index  

Itinerary Generator  
File: src/itinerarygenerator.py  
Draws day by day travelling schedules which run smoothly.  

Steps:  
	remove duplicates,  
	group places by city,  
	separate them over traveling days.  
Example output:  
Day 1 - Parthenon  
Day 2 - Acropolis Museum  
Day 3 - Ancient Agora  

Travel Video Recap Generator.  
File: src/videogenerator.py  
Libraries used:  
OpenCV  
MoviePy  
ImageIO  

Process:  
have itinerated destinations,  
load photos of those places,  
turn photos into frames,  
compose a seamless video presentation.  
Images live in:  
assets/destinations/  
Output:  
travelvideo.mp4  

AI Travel Assistant  
File: src/chatbot.py  
Using the Google Gemini API  

Capabilities:  
	answer travel queries  
	suggest destinations  
	generate plans  
explain tourist spots  

Example chat:  
User: Plan a 5 day trip in Greece  

AI: I’ve got a plan ready for you.  

PDF Travel Plan Generator  
File: src/pdfgenerator.py  
Library used:  
fpdf  

Purpose:  
Prepare an itinerary of your trip in PDF form.  

Example:  
pdf.cell(200,10,txt="Travel Itinerary",ln=True)  

Output:  
GlobeTrekTravelPlan.pdf  

Feedback Learning System  
File: src/feedbacksystem.py  
Collects:  
userquery, country, recommended sites, rating, interests, timestamp.  
Stored in:  
data/feedbacklog.csv  

Analytics Dashboard - Feedback.  
Displays statistics in the Streamlit program.  

Analytics:  
Pregnant Mothers 3.657166519703E-1) 2.0196820703E-1) 3.335839983E-1) 2.15440959067E-1) 1.86546052925E-1) 3.87773601835E-1) 1.40065362632E-1  
Top Destinations (df [[recommendedsites].valuecounts ()])  
Interest Trends ( df[ interests ].str.split(,)  

These assist in observing what is liked by people and make changes where necessary.  

Frontend Application  
File: ui/streamlitapp.py  
Framework:  
Streamlit  

Presents a user interactive interface with:  
	trip planner  
	destination explorer  
	AI chatbot  
	analytics dashboard  
	video generator  

Example UI thing:  
st.slider("Trip Duration",1,10,3)  

Project Structure  
GlobeTrekAI  

+-- data  
    +-- mastertourismdataset.csv  
    +-- feedbacklog.csv  

+-- assets  
    +-- destinations  

+-- src  
    +-- dataprocessing.py  
    +-- embeddingmodel.py  
    +-- recommenderengine.py  
    +-- locationoptimizer.py  
    +-- itinerarygenerator.py  
    +-- chatbot.py  
    +-- videogenerator.py  
    +-- pdfgenerator.py  
    +-- feedbacksystem.py  

+-- ui  
    +-- streamlitapp.py  

+-- requirements.txt  
+-- README.md  

Technologies Used  
Programming:  
Python  

AI/Machine Learning:  
Sentence Transformers  
FAISS  
Scikit-Learn  

Web Framework:  
Streamlit  

AI APIs:  
Google Gemini API  

Multimedia Processing:  
OpenCV  
MoviePy  
ImageIO  

Data Processing:  
Pandas  
NumPy  

Deployment  
Run on Streamlit Cloud.  

Deployment workflow:  
Push to GitHub repository �etto Connected to Streamlit Cloud VISA Deploy live web app.  
The requirements are read between dependencies.
