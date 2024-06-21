from transformers import pipeline
import gradio as gr

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary text"] # what type of input into model is this?
    return summary

with gr.Blocks() as demo:
    textbox = gr.Textbox(placeholder="Enter text box to summarize your shit coz u dumb af", lines=4)
    gr.Interface(fn=predict, inputs=textbox, outputs="text")

demo.launch()