#from-инструкция устанавливает базовый образ (т.е. ОС) для контейнера
FROM python:3.10-slim   
# инструкция workdir устанав. рабочий каталог для всех инструкций RUN, CMD, ENTRYPOINT, COPY и ADD, следующих за ней в файле
WORKDIR /app   
# копирование всех файлов приложения с пк в контейнер; можно реализовать копирование из github (см. документацию)
COPY . .                        
# копирование зависимостей (библиотек и моудлей)
RUN pip install -r requirements.txt 
# инструкция сообщает docker, что контейнер прослушивает указанные сетевые порты в данном случае - порт Streamlit  по умолчанию 8501
EXPOSE 8501                     
 # сообщает, как протестировать контейнер, чтобы убедиться в его работоспособности
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health  

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

