# import random libray, rock/paper/scissor game
import random
import gradio as gr

# Rock, paper, and scissor game against computer. Set a true variable for game
options = ("rock", "paper", "scissor")
game_status = True

with gr.Blocks() as demo:
    gr.Markdown(
        """
            # Rock Paper Scissors
        """
    )

    with gr.Row():
        player_choice = gr.Dropdown(['rock', 'paper', 'scissors'], label="Choose your move", multiselect=False, interactive=True,)
        
if __name__ == "__main__":
    
    demo.launch()