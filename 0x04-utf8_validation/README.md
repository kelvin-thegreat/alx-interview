## 0x04-utf8_validation Project

### Resources

#### Read or watch:
[UTF-8](https://en.wikipedia.org/wiki/UTF-8)
[Characters, Symbols, and the Unicode Miracle](https://www.youtube.com/watch?v=MijmeoH9LT4)

### Task Completed
+ [x] 0. **UTF-8 Validation**<br/>Written a method that determines if a given data set represents a valid UTF-8 encoding.The Prootype[def validUTF8(data)]( 0-validate_utf8.py)  returns `True` if data is a valid UTF-8 encoding, else return `False`
  + More requirements:
      + A character in UTF-8 can be 1 to 4 bytes long
      + The data set can contain multiple characters
      + The data will be represented by a list of integers
      + Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
    + The following code [0-main.py]( 0-main.py) is used for testing.
  ```python
      #!/usr/bin/python3
      """
      Main file for testing
      """
      
      validUTF8 = __import__('0-validate_utf8').validUTF8
      
      data = [65]
      print(validUTF8(data))
      
      data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
      print(validUTF8(data))
      
      data = [229, 65, 127, 256]
      print(validUTF8(data))
  ```

