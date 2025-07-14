import google.generativeai as genai
import os

genai.configure(api_key=os.environ.get(AIzaSyBI4XHq1lJdQZTL-S9-KLn9j2FZj09b7Ig))
model = genai.GenerativeModel("gemini-pro")

def extract_best_moments_from_transcript(transcript, jumlah=5):
    prompt = f"Dari transkrip video berikut, pilih {jumlah} momen paling menarik. Format: JSON [{{start: detik, end: detik}}].\n\n{transcript}"
    response = model.generate_content(prompt)
    return eval(response.text)  # Harap validasi data dari Gemini