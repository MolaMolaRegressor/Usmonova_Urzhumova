<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Omniscient Reader's Viewpoint Wiki</title>
    <link rel="shortcut icon" href="images/site-logo.png"/>
    <link rel="stylesheet" type="text/css" href="/static/content/bootstrap.min.css" />
    <link rel="stylesheet" type="text/css" href="/static/content/site.css" />
    <link rel="icon" href="/images/orv-logo.ico" type="image/x-icon">
    <script src="/static/scripts/modernizr-2.6.2.js"></script>
    <style>
        p {
        font-size: large;
        font-family: 'Courier New';
        font-weight:lighter;
        }

    </style>
    <style>
        h2 { 
        font-size: 120%; 
        font-family: Verdana, Arial, Helvetica, sans-serif; 
        color: #0094FF; 
       }
    </style>
    <style>
        .btn-new {
          box-shadow: 0 5px 15px 0 rgba(0, 148, 255, 1);
          transition: 0.5s;
        }

        .btn-new:hover {
          transform: translate(0,-3px);
          box-shadow: 0 20px 40px 0 rgba(0, 148, 255, 1);
        }
    </style>
</head>

<body>
    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="/" class="navbar-brand">Omniscient Reader's Viewpoint Wiki</a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="/home">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </div>
        </div>
    </div>

    <div class="container body-content">
        {{!base}}
        <hr />
        <footer>
            <p>{{ year }} - Omniscient Reader's Viewpoint Wiki. All rights belong to the authors of the work, this is an educational project only.</p>
        </footer>
    </div>

    <script src="/static/scripts/jquery-1.10.2.js"></script>
    <script src="/static/scripts/bootstrap.js"></script>
    <script src="/static/scripts/respond.js"></script>

</body>
</html>
