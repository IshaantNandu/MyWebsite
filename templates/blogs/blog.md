<style>
body {
                animation: none !important;
            }
            ul.list {
                list-style-type: none;
                text-align: center;
                font-weight: 100;
                max-width: 500px;
                word-wrap: break-word;
                margin: 0 auto;
                color: black;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                animation: none;
            }
            li.list {
                border-radius: 96px;
                border: dashed 1px #8b8b8b;
                line-height: 3;
                transform: scale(1);
                background-color: transparent;
                padding: clamp(5px, 10px, 15px);
                transition: all 516ms ease;
                margin-top: 5px;
                margin-bottom: 5px;
            }
            a.list {
                color: black;
                padding: 0.8vw;
                line-height: 3;
            }

            label {
                display: inline-block;
                transition: all 516ms ease;
            }
            label:hover {
                background: #b4b4b4;
                padding: 20px;
                border-radius: 24px;
            }

            li.list:hover {
                padding: 0.8vw;
                line-height: 3;
                background-color: #8b8b8b;
                transform: scale(1.5);
            }



            /* Add this CSS */
            .tabs {
                position: relative;
                text-align: center;
                animation: none !important;

            }

            .tabs input[type="radio"] {
                display: none;
            }


            .tabs input[type="radio"]:checked + label {
                background: #8b8b8b;
                color: white;
            }

            .tab-content {
                display: none;
                text-align: center;
                padding: 20px;
            }



            /* This ensures only the selected tab content shows */
            #tab1:checked ~ #content1,
            #tab2:checked ~ #content2,
            #tab3:checked ~ #content3 {
                display: block;
            }
            #tab1:checked,
            #tab2:checked,
            #tab3:checked {
                background: #8b8b8b;
                border-radius: 24px;
            }

            ul.navtab {
                list-style-type: none;
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: clamp(10px, 15px, 20px);
                gap: 20px;
            }

        </style>

<h1 markdown="1">My blogs:</h1>
        <ul class="navtab" markdown="1">
            <li markdown="1"><label for="tab1" markdown="1">General blogs</label></li>
            <li markdown="1"><label for="tab2" markdown="1">Tech blogs</label></li>
            <li markdown="1"><label for="tab3" markdown="1">Music blogs</label></li>
        </ul>
        <div class="tabs" markdown="1">
            <input type="radio" name="tab" id="tab1" checked markdown="1"/>
            <div class="tab-content" id="content1" markdown="1">
                <ul class="list" markdown="1">
                    <li class="list" markdown="1">
                        <a href="oldGames.html" class="list" markdown="1">
                            Ishaant's old Makecode Arcade games
                        </a>
                    </li>
                    <li class="list" markdown="1">
                        <a class="list" href="Neminath/NeminathTempleDesc.html" markdown="1"
                        >Descriptive writing on Nemināth Temple in Girnar</a
                        ><br markdown="1"/>
                    </li>
                    <li class="list" markdown="1">
                        <a class="list" href="aboutMe.html" markdown="1"
                        >About the creator of this website, Ishaant Nandu</a
                        ><br markdown="1">
                    </li>
                    <li class="list" markdown="1">
                        <a class="list" href="chessFacts.html" markdown="1">
                            Cool Chess Facts that You Probably Didn't Know
                            About</a>
                        <br markdown="1">
                    </li>
                </ul>
            </div>
            <input type="radio" name="tab" id="tab2" markdown="1"/>
            <div class="tab-content" id="content2" markdown="1">
                <ul class="list" markdown="1">
                    <li class="list" markdown="1">
                        <a class="list" href="esp32Api/esp32Api.html?v2.1" markdown="1">
                        DIY ESP32 Weather Dashboard</a
                        ><br markdown="1"/>
                    </li></ul></div></div>

                <li class="list" markdown="1">
                    <a
                        href="PyPassGenerator/PyPassGenerator.html"
                        class="list" markdown="1"
                    >
                        Python Password Generator
                    </a>
                </li>
                <li class="list" markdown="1">
                    <a href="howToMakeWebsiteBeautiful.html" class="list" markdown="1">
                        5 Ways to make your website look Cooler
                    </a>
                </li>
                <li class="list" markdown="1">
                    <a href="PyJarvis/PyJarvis.html" class="list" markdown="1">
                        DIY Jarvis in Python
                    </a>
                </li>
                <li class="list" markdown="1">
                    <a href="kustomKeypad/kustomKeypad.html" class="list" markdown="1">
                        DIY custom keypad using USB-HID
                    </a>
                </li>
            </ul>
        </div>
        <input type="radio" name="tab" id="tab3" markdown="1"/>
        <div class="tab-content" id="content3" markdown="1">
            <ul class="list" markdown="1">
                <li class="list" markdown="1">
                    <a
                        class="list"
                        href="https://ishaant.com/compositions.html" markdown="1"
                    >
                    Ishaant's compositions</a
                    ><br markdown="1"/>
                </li>
            </ul>
        </div>
    </div>
