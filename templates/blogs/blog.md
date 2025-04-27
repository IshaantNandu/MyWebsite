<br>

<div class="tab">
  <button class="tablinks" onclick="openBlog(event, 'tech')">Tech blogs</button>
  <button class="tablinks" onclick="openBlog(event, 'general')">General blogs</button>
  <button class="tablinks" onclick="openBlog(event, 'music')">Music Blogs</button>
</div>

<div id="tech" class="tabcontent">
    <a href="/esp32Api/">DIY ESP32 Weather Dashboard</a><br>
    <a href="/pyPassGenerator/">Python Password Generator</a><br>
    <a href="/pyJarvis/">DIY Python Jarvis</a><br>
    <a href="/howToMakeWebsiteBeautiful/">5 Ways to make your website look Cooler</a>
</div>

<div id="general" class="tabcontent">
    <a href="/aboutMe/">About the creator of this website, Ishaant Nandu</a><br>
    <a href="/neminathTempleDesc/">Descriptive writing on Nemināth Temple in Girnar</a><br>
    <a href="/oldGames/">Ishaant's old Makecode Arcade games</a><br>
    <a href="/chessFacts/">Chess facts that you probably didn't know</a><br>
</div>

<div id="music" class="tabcontent">
    <a href="/compositions/">Ishaant's compositions</a> <br>
</div>

<script defer>
function openBlog(evt, blogName) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
 
  document.getElementById(blogName).style.display = "block";
  evt.currentTarget.className += " active";
}

openBlog('general')
</script>