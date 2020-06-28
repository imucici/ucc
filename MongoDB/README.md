### 東西放本機端



<html lang="en">

<head>
    <meta charset="UTF-8">

    <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Lobster&amp;display=swap'>
    <link rel='stylesheet' href='https://fonts.googleapis.com/css2?family=Lobster&amp;family=Signika&amp;display=swap'>
    <link rel="stylesheet" href="https://apps.bdimg.com/libs/jqueryui/1.10.4/css/jquery-ui.min.css">
    <link rel="stylesheet" href="https://code.jquery.com/ui/1.10.4/themes/smoothness/jquery-ui.css">
    <!-- <link rel="stylesheet" type="text/css" href="public/stylesheet/style.css" charset="utf-8"> -->

    <style>
        @charset "UTF-8";

        * {
            position: relative;
            font-family: "Signika", sans-serif, 微軟正黑體;
            vertical-align: top;
        }

        html,
        body {
            width: 100%;
            height: 100%;
            margin: 0px;
            padding: 0px;
            background-color: #aaaeb5;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }



        #talking {
            opacity: 0;
            border: solid 0.5px;
            margin: 2px;
            width: 175px;
        }

        #add_id {
            position: absolute;
            top: 50px;
            left: 30px;
            margin-left: 5px;
        }

        

        .phone {
            width: 270px;
            padding: 10px;
            background-color: #f3f3f3;
            border-radius: 10px;
            transition-duration: 0.5s;
            left: 0px;
        }

        .top {
            height: 40px;
        }

        .top .camera {
            width: 10px;
            height: 10px;
            border-radius: 100%;
            background-color: #333;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
        }

        .screen {
            height: 440px;
            transition-duration: 0.5s;
            overflow: hidden;
        }

        .screen .pages {
            width: 100%;
            height: 100%;
            white-space: nowrap;
            font-size: 0px;
            transition: 0.5s;
            left: 0;
        }

        .screen .pages .page {
            background-color: #1D678F;
            font-size: initial;
            display: inline-block;
            width: 100%;
            height: 100%;
            padding: 10px;
            box-sizing: border-box;
            position: relative;
            /*   框線體積會算在本體內 */
            white-space: normal;
            color: #eee;
            font-size: 12px;
            left: 0px;
        }

        .screen .pages .page p {
            margin-top: 10px;
            letter-spacing: 2px;
            line-height: 45px;
            font-size: 50px;
            color: #34b7eb;
            left: 10px;
            text-shadow: 0.1em 0.1em #f3f3f3;
            font-weight: 900;
        }

        .screen .pages .page h2 {
            text-align: center;
            color: #a3a19e;
            font-size: 20px;
            margin: 0;
        }

        .screen .pages .page h3 {
            margin-bottom: -5px;
            font-size: 30px;
            color: #34b7eb;
            text-shadow: 0.1em 0.1em #f3f3f3;
        }

        .screen .pages .page:before {
            position: absolute;
            top: 0px;
            left: 0px;
            content: "";
            display: block;
            background-color: #92d9de;
            width: 110%;
            height: 50px;
        }

        .screen .pages .page:after {
            position: absolute;
            bottom: 0px;
            left: 0px;
            content: "";
            display: block;
            background-color: #92d9de;
            width: 110%;
            height: 30px;
            margin: -10px;
        }

        .screen .page.page1 {
            background-color: #92d9de;
            color: white;
        }

        .screen .page.page1 h2 {
            margin-top: 10px;
            font-size: 28px;
            margin-bottom: 0px;
        }

        .screen .page.page1 h1 {
            margin-top: 1px;
            font-size: 18px;
        }

        .screen .page.page1 .pic1 {
            width: 50px;
            height: 50px;
            border-radius: 100%;
            background-color: #abdcf5;
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
        }

        .screen .page.page1 .pic2 {
            width: 80px;
            height: 80px;
            border-radius: 100%;
            background-color: #bae6e2;
            position: absolute;
            left: 60%;
            top: 70%;
        }

        .screen .page.page1 .pic3 {
            width: 30px;
            height: 30px;
            border-radius: 100%;
            background-color: #babfe6;
            position: absolute;
            left: 18%;
            top: 67%;
        }

        .screen .page.page2 .icon1,
        .screen .page.page2 .icon2 {
            position: absolute;
            top: 65px;
            width: 60px;
            height: 60px;
            color: #2f5cd6;
            text-align: center;
            font-size: 50px;
            vertical-align: middle;
            display: inline-block;
            border: solid 3px #7fcce3;
            background-color: #7fcce3;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
            border-radius: 100%;
            text-shadow: 0 0 0.1em #1D678F;
        }

        .screen .page.page2 .icon1 {
            left: 70px;
        }

        .screen .page.page2 .icon2 {
            right: 65px;
        }

        .bottom {
            height: 60px;
        }

        .bottom .button {
            border: solid 1px rgba(0, 0, 0, 0.2);
            color: rgba(0, 0, 0, 0.3);
            width: 36px;
            height: 36px;
            border-radius: 100%;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 25px;
            text-align: center;
            cursor: pointer;
        }

        .bottom .button:hover {
            background-color: #ddd;
        }

        .bottom .next {
            border: solid 1px #f3f3f3;
            color: rgba(0, 0, 0, 0.3);
            width: 35px;
            height: 35px;
            border-radius: 100%;
            position: absolute;
            top: 20%;
            right: 15%;
            font-size: 25px;
            text-align: center;
            cursor: pointer;
        }

        .bottom .next:hover {
            background-color: #ddd;
        }

        .signinbtn {
            border: solid 1px;
            bottom: 110px;
            border-radius: 10px;
            display: inline-block;
            padding: 10px 10px;
            cursor: pointer;
            position: absolute;
            left: 20%;
        }

        .signinbtn:hover {
            background-color: #f5e042;
            color: #222;
            font-weight: 900;
        }

        .signupbtn {
            border: solid 1px;
            bottom: 110px;
            border-radius: 10px;
            display: inline-block;
            padding: 10px 10px;
            cursor: pointer;
            position: absolute;
            right: 20%;
        }

        .signupbtn:hover {
            background-color: #f5e042;
            color: #222;
            font-weight: 900;
        }

        .gopaybtn {
            border: solid 1px;
            margin-top: -4px;
            border-radius: 10px;
            display: inline-block;
            padding: 10px 10px;
            cursor: pointer;
            position: absolute;
            right: 36%;
        }

        .gopaybtn:hover {
            background-color: #f5e042;
            color: #222;
            font-weight: 900;
        }

        .Sender,
        .Receiver,
        .Cost {
            position: relative;
            margin: 20px 0px;
            font-size: 15px;
        }

        .Sender {
            margin-top: 30px;
        }

        .UserName {
            position: absolute;
            top: 175px;
            font-size: 15px;
        }

        .Password {
            position: absolute;
            top: 225px;
            font-size: 15px;
        }

        .account {
            width: 100px;
            height: 100px;
            border: solid 2px;
            position: absolute;
            top: 106px;
            left: 20px;
            cursor: pointer;
        }

        #pic5 {
            stroke: black;
            stroke-width: 2px;
            fill: none;
        }

        #pic5 circle {
            fill: #92d9de;
            stroke: none;
        }

        #pic5 text {
            fill: #f3f3f3;
            stroke: none;
            font-family: "Signika", sans-serif, 微軟正黑體;
            font-size: 15px;
            transition-delay: 0.5s;
        }

        #pic5 .frame_outer,
        #pic5 .frame_inner,
        #pic5 .neck,
        #pic5 .paltform {
            transform: scale(0);
            fill: #7a7671;
            transition-duration: 0.5s;
            transition-delay: 0.5s;
        }

        #pic5 .screen_content {
            opacity: 0;
            transition-duration: 0.5s;
            transition-delay: 0s;
        }

        #pic5:hover .frame_outer,
        #pic5:hover .frame_inner {
            fill: #7a7671;
            transform: scale(1);
            transition-delay: 0.5s;
        }

        #pic5:hover .neck,
        #pic5:hover .paltform {
            fill: #694f24;
            transform: scale(1);
            transition-delay: 0s;
        }

        #pic5:hover .screen_content {
            opacity: 1;
            transition-delay: 1s;
        }

        #pic5:hover text {
            opacity: 0;
            transition: 0.5s;
        }

        h4 {
            color: #f3f3f3;
            font-family: "Signika", sans-serif, 微軟正黑體;
            font-size: 15px;
            font-weight: 450;
            position: absolute;
            top: 58px;
            left: 25px;
            transition: 0.5s;
        }

        .Money {
            width: 100px;
            height: 100px;
            border: solid 2px;
            position: absolute;
            top: 107px;
            right: 21px;
            cursor: pointer;
        }

        .Money .money {
            top: 6px;
            left: 15px;
            width: 59px;
            height: 59px;
            border: solid 5px #f7e57c;
            font-size: 88px;
            color: #f7e57c;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 100%;
        }

        .Money .money:hover {
            animation: money 5s infinite;
            top: 11px;
            left: 11px;
            width: 70px;
            height: 70px;
        }

        .Money .money:hover~h4 {
            opacity: 0;
            transition: 0.5s;
        }

        @-webkit-keyframes money {
            0% {
                transform: rotate(0deg);
            }

            100% {
                transform: rotate(360deg);
            }
        }

        .Food {
            width: 100px;
            height: 100px;
            border: solid 2px;
            position: absolute;
            bottom: 100px;
            left: 21px;
            cursor: pointer;
        }

        .Food .food {
            top: 5px;
            left: 14px;
            width: 70px;
            height: 70px;
            font-size: 88px;
            color: #8f703f;
            display: flex;
            justify-content: center;
            align-items: center;
            border-radius: 100%;
            border: solid 1px #1D678F;
        }

        .Food .food:hover~h4 {
            opacity: 0;
            transition: 0.5s;
        }

        .Food .food:hover {
            animation: food 5s infinite;
        }

        @-webkit-keyframes food {
            0% {
                transform: scale(0);
            }

            100% {
                transform: scale(1);
            }
        }

        .task {
            width: 100px;
            height: 100px;
            border: solid 2px;
            position: absolute;
            bottom: 100px;
            right: 20px;
            cursor: pointer;
        }

        #pic1 {
            stroke: black;
            stroke-width: 2.7px;
        }

        #pic1 circle {
            fill: #de2d28;
        }

        #pic1 text {
            fill: #f3f3f3;
            stroke: none;
            font-family: "Signika", sans-serif, 微軟正黑體;
            font-size: 15px;
            transition-delay: 0.5s;
        }

        .task_blocks {
            position: absolute;
            top: 50px;
            left: 0px;
            width: 98%;
            height: 84%;
            overflow: auto;
            overflow-x: hidden;
        }

        .task_block {
            position: relative;
            border: solid 2px;
            border-radius: 6px;
            box-shadow: 1.3px 1.3px 1.3px #a3a19e;
            left: 23px;
            margin-top: 20px;
            width: 215px;
            height: 120px;
        }

        .task_block .task_font {
            font-size: 15px;
            font-weight: 900;
            text-decoration: underline;
            display: inline-block;
            padding: 0px;
            left: 10px;
            top: 10px;
            color: white;
        }

        .task_block .question {
            position: absolute;
            font-size: 18px;
            letter-spacing: 3px;
            font-weight: 700;
            padding: 0px;
            left: 90px;
            top: 10px;
            color: white;
        }

        /* .task_block.block2 {
  background-color: purple;
}
.task_block.block3 {
  background-color: pink;
} */

        #form1,
        #form2,
        #form3 {
            position: relative;
            top: 25px;
            left: 12px;
        }

        #q1_1,
        #q1_2,
        #q1_3,
        #q2_1,
        #q2_2,
        #q2_3,
        #q3_1,
        #q3_2,
        #q3_3 {
            width: 15px;
            height: 15px;
            margin-bottom: 3px;
            cursor: pointer;
        }

        .lb {
            font-size: 16px;
            margin-bottom: 3px;
        }

        #sub1,
        #sub2,
        #sub3 {
            color: white;
            background-color: #1D678F;
            position: absolute;
            bottom: 0px;
            left: 150px;
            border: solid 1px;
            border-radius: 8px;
            padding: 2px 6px;
            cursor: pointer;
        }


        #sub1:hover,
        #sub2:hover,
        #sub3:hover {
            background-color: #f5e042;
            color: #222;
        }
    </style>
</head>

<body translate="no">
    <meta name="”viewport”" content="”width=device-width," initial-scale="1.0″" />
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="https://apps.bdimg.com/libs/jquery/1.10.2/jquery.min.js"></script>
    <script src="https://apps.bdimg.com/libs/jqueryui/1.10.4/jquery-ui.min.js"></script>


    <div class="phone">

        <div class="top">
            <div class="camera"></div>
        </div>

        <div class="screen">
            <div class="pages">

                <div class="page page1">
                    <h3>隨便</h3>
                    <p>WALLET</p>
                    <div class="pic1"></div>
                    <div class="pic2"></div>
                    <div class="pic3"></div>
                </div>

                <div class="page page2">

                    <h2>登入 ・ 註冊
                        <div class="icon1">B</div>
                        <div class="icon2">P</div>
                    </h2>

                    <div class="UserName">🧑UserName : &nbsp &nbsp &nbsp
                        <input id="username" type="text" name="username" placeholder="ex : imucici" />
                    </div>

                    <div class="Password">🔒Password : &nbsp &nbsp &nbsp &nbsp
                        <input id="password" type="text" name="password" placeholder="ex : 12345" />
                    </div>

                    <div class="signinbtn" onclick="login()">登入 ➜</div>
                    <div class="signupbtn" onclick="signup()">註冊 ➜</div>

                </div>

                <div class="page page3">
                    <h2>今天想幹嘛</h2>

                    <div class="account">
                        <SVG id="pic5" viewbox="-50 -40 100 100">

                            <rect class="frame_outer" x="-30" y="-20" width="60" height="40"></rect>
                            <rect class="frame_inner" x="-25" y="-15" width="50" height="30"></rect>
                            <rect class="neck" x="-2" y="20" width="4" height="10"></rect>
                            <rect class="paltform" x="-10" y="30" width="20" height="5"></rect>

                            <g class="screen_content">
                                <line x1="-20" y1="0" x2="-8" y2="0"></line>
                                <line x1="-20" y1="5" x2="-4" y2="5"></line>
                                <circle cx="10" cy="0" r="7"></circle>
                            </g>

                            <text class="text" x="-28" y="53">我的帳戶</text>
                        </SVG>
                    </div>

                    <div class="Money">
                        <div class="money">$ </div>
                        <h4> 轉 帳 $</h4>
                    </div>

                    <div class="Food">
                        <div class="food"> 🍽</div>
                        <h4>吃什麼 ? </h4>
                    </div>

                    <div class="task">
                        <SVG id="pic1" viewbox="-50 -50 100 100">
                            <line x1="-26" y1="0" x2="26" y2="0"></line>
                            <line x1="0" y1="26" x2="0" y2="-26"></line>
                            <circle cx="0" cy="0" r="8">
                                <animate attributeName="r" dur="2s" values="17;13;17" repeatCount="indefinite">
                                </animate>
                            </circle>
                            <text class="text" x="-29" y="44">每日任務</text>
                        </SVG>
                    </div>
                </div>


                <div class="page page4">
                    <h2>轉帳(顯示當筆交易明細)</h2>

                    <div class="Sender">Sender : &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
                        <input id="sen" type="text" name="sender" placeholder="ex : imucici" />
                    </div>

                    <div class="Receiver">Receiver : &nbsp &nbsp &nbsp &nbsp &nbsp
                        <input id="rev" type="text" name="receiver" placeholder="ex : imucici" />
                    </div>

                    <div class="Cost">Cost : &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp &nbsp
                        <input id="cost" type="text" name="Cost" placeholder="ex : 1" />
                    </div>

                    <div class="gopaybtn" onclick="pay()">GoPay !</div>

                </div>

                <div class="page page5">
                    <h2>每日任務</h2>
                    <div class="task_blocks">

                        <!-- <div id="dialog">
            <p style="text-align: center">₿+1</p>
          </div> -->

                        <div class="task_block block1">
                            <div class="task_font">#1 </div>
                            <div class="question">gender?</div>
                            <form id="form1">
                                <input id="q1_1" type="radio" value="male" name="question1" />
                                <label class="lb" for="male">Male</label><br />
                                <input id="q1_2" type="radio" value="female" name="question1" />
                                <label class="lb" for="female">Female</label><br />
                                <input id="q1_3" type="radio" value="other" name="question1" />
                                <label class="lb" for="other">Other</label><br />
                                <input id="sub1" type="button" value="確認" />
                            </form>
                        </div>
                        <div class="task_block block2">
                            <div class="task_font">#2</div>
                            <div class="question">2+2=?</div>
                            <form id="form2">
                                <input id="q2_1" type="radio" value="4" name="question2" />
                                <label class="lb" for="4">4</label><br />
                                <input id="q2_2" type="radio" value="8" name="question2" />
                                <label class="lb" for="8">8</label><br />
                                <input id="q2_3" type="radio" value="0" name="question2" />
                                <label class="lb" for="0">0</label><br />
                                <input id="sub2" type="button" value="確認" />
                            </form>
                        </div>
                        <div class="task_block block3">
                            <div class="task_font">#3</div>
                            <div class="question">問題3</div>
                            <form id="form3">
                                <input id="q3_1" type="radio" value="ans1" name="question3" />
                                <label class="lb" for="ans1">ans1</label><br />
                                <input id="q3_2" type="radio" value="ans2" name="question3" />
                                <label class="lb" for="ans2">ans2</label><br />
                                <input id="q3_3" type="radio" value="ans3" name="question3" />
                                <label class="lb" for="ans3">ans3</label><br />
                                <input id="sub3" type="button" value="確認" />
                            </form>
                        </div>
                    </div>

                </div>

                <div class="page page6">
                    <h2>我的帳戶</h2>






                </div>

                <div class="page page7">
                    <h2>討論版</h2>

                    <div class='CRUD add_area'>

                        <form action="http://127.0.0.1:8081/add_one" method="POST">

                            <input type="text" id="talking" name="talking" placeholder="請輸入訊息...">

                            <input type="submit" id="add_id" value="前往聊天室">
                        </form>
                    </div>
                    <!-- <div class="load_talks"></div> -->





                </div>





            </div>
        </div>

        <div class="bottom">
            <div class="button">☐</div>
            <div class="next">▷ </div>
        </div>

    </div>

    <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/3.5.0/jquery.min.js'></script>
    <script id="rendered-js">
        

        var page = 0;
        $(".next").click(function () {
            page += 1;
            if (page > 6) {
                page = 0;
            }
            $(".pages").css("left", "-" + page * 100 + "%");
            // screen_audio.play();
        });

        $(".button").click(function () {
            // home_audio.play();
            var page_conut = 0;
            page_conut += 2;
            $(".pages").css("left", "-" + page_conut * 100 + "%");

        });

    </script>
</body>

</html>
