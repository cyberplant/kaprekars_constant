#!/usr/bin/env python3
"""
Kaprekar's Constant Explorer

This script explores Kaprekar's constant (6174) by taking a 4-digit number
with no repeated digits and repeatedly applying the Kaprekar process:
1. Sort digits in descending order (A)
2. Sort digits in ascending order (B) 
3. Calculate A - B
4. Repeat until reaching 6174 or hitting the step limit

The script uses the rich library for beautiful console output.
"""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt
from rich import print as rprint

console = Console()

def validate_input(number_str):
    """
    Validate that the input is a 4-digit number with no repeated digits.
    
    Args:
        number_str (str): The input string to validate
        
    Returns:
        tuple: (is_valid, error_message, number)
    """
    # Check if it's a valid integer
    try:
        number = int(number_str)
    except ValueError:
        return False, "Input must be a valid number", None
    
    # Check if it's 4 digits
    if number < 1000 or number > 9999:
        return False, "Number must be exactly 4 digits", None
    
    # Check for repeated digits
    digits = list(str(number).zfill(4))
    if len(set(digits)) != 4:
        return False, "All 4 digits must be different (no repeated digits)", None
    
    return True, None, number

def kaprekar_step(number):
    """
    Perform one step of the Kaprekar process.
    
    Args:
        number (int): The current number
        
    Returns:
        int: The result of A - B where A is digits sorted descending, B is ascending
    """
    # Convert to 4-digit string with leading zeros if needed
    number_str = str(number).zfill(4)
    
    # Sort digits in descending order (A)
    digits_desc = sorted(number_str, reverse=True)
    A = int(''.join(digits_desc))
    
    # Sort digits in ascending order (B)
    digits_asc = sorted(number_str)
    B = int(''.join(digits_asc))
    
    return A - B

def explore_kaprekar(starting_number, max_steps=50):
    """
    Explore Kaprekar's constant starting from a given number.
    
    Args:
        starting_number (int): The starting 4-digit number
        max_steps (int): Maximum number of steps to try
        
    Returns:
        tuple: (steps, sequence, reached_constant)
    """
    sequence = [starting_number]
    current_number = starting_number
    steps = 0
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        console=console,
        transient=True
    ) as progress:
        task = progress.add_task("Exploring Kaprekar's constant...", total=None)
        
        while steps < max_steps:
            if current_number == 6174:
                progress.update(task, description="Found Kaprekar's constant!")
                break
                
            next_number = kaprekar_step(current_number)
            sequence.append(next_number)
            current_number = next_number
            steps += 1
            
            progress.update(task, description=f"Step {steps}: {current_number}")
    
    reached_constant = (current_number == 6174)
    return steps, sequence, reached_constant

def display_results(starting_number, steps, sequence, reached_constant):
    """
    Display the results in a beautiful format using rich.
    """
    console.print("\n" + "="*60)
    
    # Main result panel
    if reached_constant:
        result_text = Text("SUCCESS!", style="bold green")
        result_text.append(f"\nReached Kaprekar's constant (6174) in {steps} steps")
    else:
        result_text = Text("LIMIT REACHED", style="bold yellow")
        result_text.append(f"\nDid not reach 6174 within {steps} steps")
    
    console.print(Panel(
        result_text,
        title="[bold blue]Kaprekar's Constant Explorer Results[/bold blue]",
        border_style="blue"
    ))
    
    # Sequence table
    table = Table(title="Step-by-Step Sequence", show_header=True, header_style="bold magenta")
    table.add_column("Step", style="cyan", width=6)
    table.add_column("Number", style="green", width=8)
    table.add_column("Process", style="yellow", width=40)
    
    for i, number in enumerate(sequence):
        if i == 0:
            table.add_row("Start", str(number), "Initial number")
        else:
            # Show the Kaprekar process for this step
            number_str = str(sequence[i-1]).zfill(4)
            digits_desc = sorted(number_str, reverse=True)
            digits_asc = sorted(number_str)
            A = int(''.join(digits_desc))
            B = int(''.join(digits_asc))
            process = f"{A} - {B} = {number}"
            
            if i == len(sequence) - 1 and reached_constant:
                process += " 🎉 KAPREKAR'S CONSTANT!"
            
            table.add_row(str(i), str(number), process)
    
    console.print(table)
    
    # Summary statistics
    console.print(f"\n[bold]Starting number:[/bold] {starting_number}")
    console.print(f"[bold]Total steps:[/bold] {steps}")
    console.print(f"[bold]Final number:[/bold] {sequence[-1]}")
    console.print(f"[bold]Reached 6174:[/bold] {'Yes' if reached_constant else 'No'}")

def main():
    """Main function to run the Kaprekar's constant explorer."""
    console.print(Panel(
        "[bold blue]Welcome to Kaprekar's Constant Explorer![/bold blue]\n\n"
        "This program explores the fascinating mathematical phenomenon where\n"
        "any 4-digit number with different digits eventually reaches 6174\n"
        "through a simple process of sorting and subtracting.\n\n"
        "[yellow]Enter a 4-digit number with all different digits[/yellow]",
        title="🔢 Kaprekar's Constant Explorer",
        border_style="blue"
    ))
    
    while True:
        try:
            # Get input from user
            number_str = Prompt.ask("\n[bold cyan]Enter a 4-digit number[/bold cyan]")
            
            # Validate input
            is_valid, error_msg, number = validate_input(number_str)
            
            if not is_valid:
                console.print(f"[bold red]Error:[/bold red] {error_msg}")
                continue
            
            # Explore Kaprekar's constant
            steps, sequence, reached_constant = explore_kaprekar(number)
            
            # Display results
            display_results(number, steps, sequence, reached_constant)
            
            # Ask if user wants to try another number
            another = Prompt.ask("\n[bold cyan]Try another number?[/bold cyan]", choices=["y", "n", "yes", "no"], default="y")
            if another.lower() in ["n", "no"]:
                break
                
        except KeyboardInterrupt:
            console.print("\n\n[yellow]Goodbye![/yellow]")
            break
        except Exception as e:
            console.print(f"[bold red]Unexpected error:[/bold red] {e}")
            break
    
    console.print("\n[bold green]Thank you for exploring Kaprekar's constant![/bold green]")

if __name__ == "__main__":
    main()
