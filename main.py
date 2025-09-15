# import random libray, rock/paper/scissor game
import random
import gradio as gr

# Rock, paper, and scissor game against computer. Set a true variable for game
options = ("rock", "paper", "scissor")
game_status = True

player_wins = 0
computer_wins = 0

with gr.Blocks() as demo:
    gr.Markdown(
        """
            # Rock Paper Scissors
            
        """
    )
    
    gr.Markdown(
        f"""
            | Human | Computer | 
            | -------| ------|
            | 👤 | 🤖 | 
            | {player_wins} | {computer_wins} |
        """
    )
    

    with gr.Row():
        player_choice = gr.Dropdown(['rock', 'paper', 'scissors'], label="Choose your move", multiselect=False, interactive=True,)
    
    with gr.Row():
        play_btn = gr.Button("Play Round")
        play_btn.click()
        
        
if __name__ == "__main__":
    
    demo.launch()