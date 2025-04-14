# 5 Ways to make your website look Cooler

What you will need-

*   a computer running Windows, Linux or MacOs
*   Basic knowledge of HTML, CSS and Javascript

### Abstract

Websites have become the Swiss Army knife of the digital era. They're globally used by brands and companies, but also for personal use. You can [create your own website](https://www.wikihow.com/Make-a-Website) learning [HTML](https://www.w3schools.com/html/default.asp), [CSS](https://www.w3schools.com/css/default.asp) and [JavaScript](https://www.w3schools.com/js/default.asp), buying your own server (My dad bought me a server), buying a [Domain Name](https://www.godaddy.com/en-in) (website name) and then configuring [Apache](https://ubuntu.com/tutorials/install-and-configure-apache#1-overview) or [Nginx](https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-22-04) on your server. Now, you may want your website to look fancy, so here are some code snippets to make your Website cooler.

1. ### Add smooth scrolling
When you scroll a HTML page, it may look weird, fast, or
unresponsive to your scrolling By just adding this line of code to your CSS, your HTML page will scroll smoother. Additionally,
anchor-links like `:::html <a href="#Hyperlink">Click me Anchor Link</a><aside>Some content here......</aside><p id="Hyperlink">Here's the Anchor Link&lt;p&gt;                  element</p>` will automatically give a smooth scrolling effect, almost like you're manually scrolling down to a certain HTML element. So here's the CSS code for smooth scrolling:
```css
html{
    scroll-behavior:smooth;
}
```
2. ### Animations
If you've seen my website (you obviously have) 
you might've noticed that there are animations in it. 
Animations are actually pretty easy to implement in CSS. 
All that you have to do is use the `@Keyframes` rule and 
implement it in an element. Here's my sample `@Keyframes` rule:-
```css
@keyframes fadein{
    0%{
        /*
        Your starting properties go here: like
        */
        opacity:0;
        transform:scale(0.5);
    }
    100%{
        /*
        Your ending properties go here: like
        */
        opacity:1;
        transform:scale(1);
    }
}

```
Now, all you have to do is implement it in an element using the shorthand
`animation` property or using the `animation-name:/*insert animation-name*/;`, 
`animation-duration:/*insert animation-duration*/;`, `animation-timing-function:/*insert timing function*/;`
and `animation-delay:/*insert animation-delay*/;` properties. 
