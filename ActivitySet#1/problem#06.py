#strings
def myinput():
  text = "x-DSPAM-confidence:  0.8475"
  return text

def convert(text):
  pos = text.find(':')
  last = text[pos+1:]
  end = float(last)
  return(end)

def output(end):
    
    print(end)

def main():
  text=myinput()
  end=convert(text)
  output(end)
     
main()
