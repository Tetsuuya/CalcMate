import numpy as np
import sympy as sp

def parse_expression(expr_str):
    """Convert user input to proper mathematical expression"""
    try:
        # Replace common math notations with proper syntax
        expr_str = expr_str.replace(' ', '')  # Remove spaces
        
        # Handle implicit multiplication (e.g., 2x -> 2*x)
        modified = ''
        for i in range(len(expr_str)):
            if i > 0:
                # Handle cases like 2x, 3x^2, etc.
                if (expr_str[i].isalpha() and (expr_str[i-1].isdigit() or expr_str[i-1] == ')')) or \
                   (expr_str[i] == '(' and (expr_str[i-1].isdigit() or expr_str[i-1].isalpha() or expr_str[i-1] == ')')):
                    modified += '*'
            modified += expr_str[i]
        
        # Handle other common mathematical functions
        modified = modified.replace('^', '**')  # Handle power notation
        
        # Validate the expression contains 'x' variable
        if 'x' not in modified:
            modified = modified + '*x**0'  # Make it a function of x
            
        # Print for debugging
        print(f"Input: {expr_str} -> Parsed: {modified}")
        return modified
    except Exception as e:
        print(f"Error parsing expression: {e}")
        return expr_str  # Return original string if parsing fails

def format_expression(expr):
    """Convert sympy expression to readable format"""
    # Convert the expression to a string
    expr_str = str(expr)
    # Replace ** with ^
    expr_str = expr_str.replace('**', '^')
    # Replace multiplication with simpler format
    expr_str = expr_str.replace('*', '')
    return expr_str

def calculate_derivative(expr_str, x_vals):
    """Calculate both symbolic and numerical derivative"""
    x = sp.Symbol('x')
    try:
        # Parse and convert string to symbolic expression
        expr_str = parse_expression(expr_str)
        expr = sp.sympify(expr_str)
        # Get symbolic derivative
        derivative = sp.diff(expr, x)
        # Convert to numerical function using numpy for vectorized operations
        derivative_lambda = sp.lambdify(x, derivative, modules=['numpy'])
        # Calculate numerical values
        try:
            numerical_result = derivative_lambda(x_vals)
            if not isinstance(numerical_result, np.ndarray):
                numerical_result = np.full_like(x_vals, numerical_result)
        except Exception as e:
            print(f"Numerical evaluation error: {e}")
            return None, "Error in calculation"
        # Format the derivative expression
        derivative_str = format_expression(derivative)
        return numerical_result, derivative_str
    except Exception as e:
        print(f"Derivative calculation error: {e}")
        return None, "Error in calculation"

def calculate_integral(expr_str, lower, upper):
    """Calculate both symbolic and definite integral"""
    x = sp.Symbol('x')
    try:
        # Parse and convert string to symbolic expression
        expr_str = parse_expression(expr_str)
        expr = sp.sympify(expr_str)
        # Get symbolic integral
        integral = sp.integrate(expr, x)
        # Convert to numerical function
        integral_lambda = sp.lambdify(x, integral, modules=['numpy'])
        # Calculate definite integral
        definite_integral = float(integral_lambda(upper) - integral_lambda(lower))
        # Format the integral expression
        integral_str = format_expression(integral)
        return integral_lambda, definite_integral, integral_str
    except Exception as e:
        print(f"Integration calculation error: {e}")
        return None, None, "Error in calculation"

def evaluate_function(expr_str, x_vals):
    """Evaluate the original function"""
    x = sp.Symbol('x')
    try:
        # Parse and convert string to symbolic expression
        expr_str = parse_expression(expr_str)
        expr = sp.sympify(expr_str)
        func = sp.lambdify(x, expr, modules=['numpy'])
        result = func(x_vals)
        
        # Convert result to numpy array and handle scalar results
        result = np.asarray(result)
        if result.ndim == 0:  # scalar result
            result = np.full_like(x_vals, float(result))
        return result
    except Exception as e:
        print(f"Function evaluation error: {e}")
        return None 