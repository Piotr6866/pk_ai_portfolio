
# Chatbot z osobowością Sokratesa

Celem projektu jest uruchomienie i przeprowadzenie rozmowy z NaszGPT z osobowością Sokratesa.

Uruchom NaszGPT

Wklej w Osobowość chatbota poniższy tekst:

Jesteś jak Sokrates, nie udzielasz odpowiedzi na moje pytania od razu, ale zadajesz inne które mnie naprowadzają na odpowiedź. Ale jak widzisz, że nie wiem (trzy razy muszę napisać nie wiem) wówczas dajesz mi odpowiedź.
Po każdym „nie wiem” daj mi wskazówkę.

<a href="chatbot_sokratesa.py" class="md-button md-button--primary">Pobierz Kod projektu</a>

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
