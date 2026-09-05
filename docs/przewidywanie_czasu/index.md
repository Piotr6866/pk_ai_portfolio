
# Przewidywanie czasu ukończenia półmaratonu

Zaimplementowanie aplikacji szacującej czas ukończenia półmaratonu dla zadanych danych

1. Umieść dane w Digital Ocean Spaces
2. Napisz notebook, który będzie Twoim pipelinem do trenowania modelu
    * czyta dane z Digital Ocean Spaces
    * czyści je
    * trenuje model (dobierz odpowiednie metryki [feature selection])
    * nowa wersja modelu jest zapisywana lokalnie i do Digital Ocean Spaces
3. Aplikacja
    * opakuj model w aplikację streamlit
    * wdróż (deploy) aplikację za pomocą Digital Ocean AppPlatform 
    * wejściem jest pole tekstowe, w którym użytkownik się przedstawia, mówi o tym jaka jest jego płeć, wiek i czas na 5km
    * jeśli użytkownik podał za mało danych, wyświetl informację o tym jakich danych brakuje
    * za pomocą LLM (OpenAI) wyłuskaj potrzebne dane, potrzebne dla Twojego modelu do określenia, do słownika (dictionary lub JSON)
    * Tę część podepnij do Langfuse, aby zbierać metryki o skuteczności działania LLM’a

<a href="app.py" class="md-button md-button--primary">Pobierz Kod projektu</a>

<a href="https://github.com/Piotr6866/zadanie_modul_9" class="md-button md-button--primary">Link do kodu na github</a>

<script>
function resizeIframeToFitContent(iframe) {
    iframe.style.height = (iframe.contentWindow.document.documentElement.scrollHeight + 50) + "px";
    iframe.contentDocument.body.style["overflow"] = 'hidden';
}
window.addEventListener('load', function() {
    var iframe = document.getElementById('content');
    resizeIframeToFitContent(iframe);
});
window.addEventListener('resize', function() {
    var iframe = document.getElementById('content');
    resizeIframeToFitContent(iframe);
});
</script>
