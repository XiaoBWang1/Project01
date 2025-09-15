import gradio as gr

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
