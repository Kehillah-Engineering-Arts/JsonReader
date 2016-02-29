import json
class reader():
    def __init__(self, filename):
        self.filename = filename
        with open(filename) as f:
            self.qandas = json.load(f)


    def __str__(self):
        return "==[ start '{0}' ]==\n{1}\n==[  end  '{0}' ]==".format(self.filename, self.qandas)

    def checkanswers(self, answers):
        """ 
        answers are a dict in {question#: answer#, ...}
        """
        if not isinstance(answers, dict):
            raise ValueError('Can only check answers on type dict, not type \'%s\'' % type(answers))
        incorrect = set()
        for question in answers:
            if str(question) not in self.qandas:
                print("Warning! Question #{} is out of bounds (max:{})".format(question, max(self.qandas.keys())))
                continue
            if self.qandas[str(question)]['correct'] != answers[question]:
                incorrect.add(question)
        return incorrect


if __name__ == '__main__':
    def writetestfile(filename):
        json.dump(
          {
            0:{'question':'what is the meaning of life?',
                'answers':{0:'42', 1:'pie', 2:'yes', 3:'n/a'},
                'correct':0
              },
            1:{'question':'who is a good boy?',
                'answers':{0:'Everyone!', 1:'me? is it me?', 2:'I am!'},
                'correct':1
              },
            2:{'question':'what is the best colour?',
                'answers':{0:'black', 1:'white', 2:'blue', 3:'green', 4:'red'},
                'correct':3
              },
          }, 
            open(filename, 'w'),
            indent = 2
        )
    writetestfile('testdata.json')
    r = reader('testdata.json')
    print(r.checkanswers({0:0, 1:2, 2:3}))
    print(r)