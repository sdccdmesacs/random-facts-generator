# 1.Instructions:

a) Please go to website: https://www.api-ninjas.com/api/facts

b) Sign up for a free api-ninjas account and get your API key.

c) Comeback to Facts API

d) Scroll down to Code Examples

> I used Python for this project even though I have a Java file in this folder because the Java code that used to interact with this API doesn't work at all. The issue happened with this line: 
```java
import com.fasterxml.jackson.databind.ObjectMapper;
```

e) If anyone uses Python, please notice that I had to update the code a litle bit to make it work. If you use my code, please replace 'your_api_key_here' on the line below with your actual API key.

```python
response = requests.get(api_url, headers={'X-Api-Key': 'your_api_key_here'})
```
>* Code Example After Replacing the API key:

```python
response = requests.get(api_url, headers={'X-Api-Key': 'werwesdfdsdsgsg4858622'})
```
<br>

* Another notice is that response.text will return a string that looks like this:
```python
"{"fact":"Pucks hit by hockey sticks have reached speeds of up to 150 miles per hour"}"
```
* So I had to use json.loads() to convert it into a list, then access the first element of the list to get the fact based on the "fact" key of the dictionary inside it.


<br>

# 2.Output:

> Example #1:
```Shell
python Main.py
Pucks hit by hockey sticks have reached speeds of up to 150 miles per hour
```
<br>

> Example #1:
```Shell
python Main.py
Cinderella is known as Rashin Coatie in Scotland, Zezolla in Italy, and Yeh-hsien in China
```