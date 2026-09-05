
# Łączenie danych klienta:

Zapraszam do zapoznania się z projektem mojego autorstwa, Wykonuję w nim zlecenia dla firmy, która chce żebym połączył dane z trzech różnych źródeł.

Pierwsze źródło danych to dane o klientach. Na szczęście zespół, który zajmuje się klientami, wie co robi i wszystkie dane dostępne są w bazie danych (zad_domowe__clients.db w tabeli clients).
Drugie źródło danych to dane o produktach. W tym przypadku dane dostępne są w pliku CSV (zad_domowe__products.csv).
Ostatnie źródło danych to dane o zamówieniach / fakturach. Tutaj niestety mamy problem. Okazuje się, że klient wszystkie faktury ma w postaci zrzutów z ekranu (pliki zad_domowe__invoice_1.png, zad_domowe__invoice_2.png etc.).
Twoim zadaniem jest połączenie tych danych w jeden plik CSV, który będzie zawierał informacje o kliencie, produkcie i fakturze. Przygotuj plik CSV, który zawiera tylko niezbędne kolumny, nie ma żadnych kolumn powtórzonych.

Jak rezultat wyciągania danych z faktur chcę mieć w każdym wierszu informacje o zakupionym produkcie, ilości, kliencie, cenie jednostkowej.

<a href="laczenie_danych.ipynb" class="md-button md-button--primary">Pobierz Notebook</a>

<iframe
    id="content"
    src="laczenie_danych.html"
    width="100%"
    style="border:1px solid black;overflow:hidden;"
></iframe>
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
