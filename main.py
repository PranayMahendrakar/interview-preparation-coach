#!/usr/bin/env python3
"""Interview Preparation Coach - Author: Pranay M"""
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt
from rich.markdown import Markdown
from modules import QuestionGenerator, AnswerEvaluator, MockInterviewer, FeedbackProvider

console = Console()

def main():
    console.print(Panel("🎯 INTERVIEW PREPARATION COACH 🎯\nAce Your Next Interview", style="bold red"))
    
    mods = [("Generate Questions", QuestionGenerator()), ("Evaluate Answer", AnswerEvaluator()),
            ("Mock Interview", MockInterviewer()), ("Get Feedback", FeedbackProvider())]
    
    while True:
        table = Table(title="Interview Tools")
        for i,(n,_) in enumerate(mods,1): table.add_row(str(i), n)
        table.add_row("0", "Exit")
        console.print(table)
        
        c = Prompt.ask("Select", choices=["0","1","2","3","4"])
        if c == "0": break
        
        idx = int(c) - 1
        if idx == 0:
            role = Prompt.ask("Job role")
            result = mods[idx][1].process(f"Generate interview questions for {role}")
        elif idx == 1:
            answer = Prompt.ask("Your answer to evaluate")
            result = mods[idx][1].process(answer)
        elif idx == 2:
            role = Prompt.ask("Role to practice")
            console.print("[yellow]Mock interview starting...[/yellow]")
            question = mods[idx][1].process(f"Ask first interview question for {role}")
            console.print(Panel(question, title="Interviewer", border_style="blue"))
            answer = Prompt.ask("Your response")
            result = AnswerEvaluator().process(f"Question: {question}\nAnswer: {answer}")
        else:
            area = Prompt.ask("Area for feedback")
            result = mods[idx][1].process(area)
        
        console.print(Panel(Markdown(str(result)), title=mods[idx][0], border_style="red"))

if __name__ == "__main__": main()
