# text_to_image_pipeline.py

import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os

# Load the Stable Diffusion model
def load_model(model_name: str = "CompVis/stable-diffusion-v1-4") -> StableDiffusionPipeline:
    """
    Load the Stable Diffusion model for text-to-image generation.

    Parameters:
        model_name (str): The name of the pre-trained model.

    Returns:
        StableDiffusionPipeline: Loaded model ready for inference.
    """
    pipe = StableDiffusionPipeline.from_pretrained(model_name, torch_dtype=torch.float16)
    pipe = pipe.to("cuda")  # Move the model to GPU if available
    return pipe

def generate_image(pipe: StableDiffusionPipeline, prompt: str, output_dir: str, image_name: str) -> None:
    """
    Generate an image from a text prompt using the provided model.

    Parameters:
        pipe (StableDiffusionPipeline): The loaded model.
        prompt (str): The text prompt for image generation.
        output_dir (str): Directory to save the generated image.
        image_name (str): Name of the output image file.
    """
    with torch.no_grad():
        image = pipe(prompt).images[0]  # Generate image
    # Save the generated image
    os.makedirs(output_dir, exist_ok=True)
    image.save(os.path.join(output_dir, image_name))

if __name__ == "__main__":
    model = load_model()  # Load the model
    prompt = "A laboratory setting with scientists conducting research on cancer treatment."
    output_directory = "generated_images"
    image_file_name = "cancer_research.png"
    
    print(f"Generating image for prompt: '{prompt}'")
    generate_image(model, prompt, output_directory, image_file_name)
    print(f"Image saved at {output_directory}/{image_file_name}")

