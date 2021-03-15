import requests
from concurrent.futures import ThreadPoolExecutor

class TextComparer:
    
    def __init__(self, url_list):
        self.filenames = []
        self.num = 0
        self.url_list = url_list

    def download(self, url, filename):
        rs = requests.get(url)
        if (rs.status_code == 404):
            raise NotFoundException()

        with open( 'modules/week_6/'+filename, 'wb') as f:
            for chunk in rs.iter_content(chunk_size=1024):
                f.write(chunk)

    def multi_download(self):
        folder = 'modules/week_6/'
        for index,val in enumerate(self.url_list):
            s = 'dillermand'+str(index)+".txt"
            self.filenames.append(s)
        workers=5
        with ThreadPoolExecutor(workers) as ex:
            ex.map(self.download, self.url_list, self.filenames)
    
    def __iter__(self):
        return self

    def __next__(self):
        if (self.num <= len(self.filenames)):
            num = self.num
            self.num +=1
            return self.filenames[num]
        else:
            self.num = 0
            raise StopIteration
