import requests


def main(first_url):
    def helper(index):
        print('index is ' + str(index))
        url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(index)
        content = requests.get(url).text
        print('content is ' + content)
        try:
            new_index = int(content.split()[-1])
            return(helper(new_index))
        except:
            return content


    print(helper(8022))


if __name__ == '__main__':
    main('')
