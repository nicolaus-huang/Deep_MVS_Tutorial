FROM nablascom/cuda-pytorch

COPY . .

RUN pip3 install -r ./requirements.txt

CMD [ "sh", "-c", "./custom_para.sh" ]