# main_pipeline.py

from data_preprocessing import clean_and_tokenize_data
from text_summarization import summarize_text
from text_to_image_pipeline import load_model, generate_image
from logger import log_info, log_error

def main():
    try:
        # Step 1: Load and preprocess data
        log_info("Starting data preprocessing...")
        raw_data = "Your raw text data goes here."  # Replace with actual data loading
        processed_data = clean_and_tokenize_data(raw_data)
        log_info("Data preprocessing completed.")

        # Step 2: Summarize the processed text
        log_info("Starting text summarization...")
        summarized_text = summarize_text(processed_data)
        log_info("Text summarization completed.")
        log_info(f"Summarized Text: {summarized_text}")

        # Step 3: Generate an image based on the summarized text
        log_info("Starting text-to-image generation...")
        model = load_model()  # Load the model
        output_directory = "generated_images"
        image_file_name = "pharma_research.png"
        
        generate_image(model, summarized_text, output_directory, image_file_name)
        log_info(f"Image generated and saved at {output_directory}/{image_file_name}.")
        
    except Exception as e:
        log_error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()


