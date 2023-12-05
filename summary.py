from flask import Flask, render_template, request, jsonify
import numpy as np
from transformers import TFBartForConditionalGeneration, BartTokenizer, pipeline
import tensorflow
app = Flask(__name__, template_folder="templates")

model = TFBartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn", local_files_only=True)
tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn", local_files_only=True)
summarizer= pipeline("summarization",model=model, tokenizer=tokenizer)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == "POST":
        text = request.form["text"]
        #inputs = tokenizer(text, return_tensors='pt', max_length=1024, truncation=True)

         # Convert the tensors to NumPy arrays
        #input_ids_np = inputs['input_ids'].numpy()
        #attention_mask_np = inputs['attention_mask'].numpy()

        #print(f"Original Text: {inputs}")
        summary = summarizer(text, max_length=150, min_length=50, length_penalty=2.0)
        text = summary[0]['summary_text']
        text = text.split()
        n = 10
        output = [' '.join(text[i:i+n]) for i in range(0, len(text), n)]
        return render_template('index.html', output=output)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)