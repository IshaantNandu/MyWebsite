<br>

<div class="tab">
  <button class="tablinks" onclick="open(event, 'tech')">Tech blogs</button>
  <button class="tablinks" onclick="open(event, 'general')">General blogs</button>
  <button class="tablinks" onclick="open(event, 'music')">Music Blogs</button>
</div>

<div id="tech" class="tabcontent">
    <a href="/esp32Api/">ESP32 Api</a>
    <a href="/pyPassGenerator/">Python Password Generator</a>
    <a href="/howToMakeWebsiteBeautiful/">5 Ways to make your website look Cooler</a>
</div>

<div id="general" class="tabcontent">
    <a href="/esp32Api/">ESP32 Api</a>
    <a href="/pyPassGenerator/">Python Password Generator</a>
    <a href="/howToMakeWebsiteBeautiful/">5 Ways to make your website look Cooler</a>
</div>

<div id="music" class="tabcontent">
    <a href="/esp32Api/">ESP32 Api</a>
    <a href="/pyPassGenerator/">Python Password Generator</a>
    <a href="/howToMakeWebsiteBeautiful/">5 Ways to make your website look Cooler</a>
</div>

<script>
function open(evt, cityName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(cityName).style.display = "block";
  evt.currentTarget.className += " active";
}
</script>