# import random libray, rock/paper/scissor game
import random
import gradio as gr

# Rock, paper, and scissor game against computer. Set a true variable for game
options = ("rock", "paper", "scissor")
game_status = True

with gr.Blocks() as demo:
    gr.Markdown(
        """
            Rock Paper Scissors
        """
    )

        
if __name__ == "__main__":
    
    demo.launch()