### Tasks Completed
+ [x] 0. **Pascal's Triangle**<br/>Create a function[def pascal_triangle(n)](0-pascal_triangle.py) that returns a list of lists of integers
  + representing the Pascal's triangle of [n]:
    + returns an empty list if `n<=0`.
    + you can assume `n` will always be an integer
    + The following code is used for testing.
  ```python
  #!/usr/bin/python3
  """
  0-main
  """
  pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

  def print_triangle(triangle):
      """
      Print the triangle
      """
      for row in triangle:
          print("[{}]".format(",".join([str(x) for x in row])))


  if __name__ == "__main__":
      print_triangle(pascal_triangle(5))
  ```
