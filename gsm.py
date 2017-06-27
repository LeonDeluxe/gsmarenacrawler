from BeautifulSoup import BeautifulSoup
import re

input = '''
<!doctype html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US" lang="en-US">
<head>
<title>Apple iPhone 7 - Full phone specifications</title>
<link rel="stylesheet" href="http://cdn.gsmarena.com/vv/assets9/css/gsmarena.css?v=41">
<!--[if lt IE 9]>
<script src="http://ie7-js.googlecode.com/svn/version/2.1(beta4)/IE9.js"></script>
<![endif]-->


<!-- Begin Cookie Consent plugin by Silktide - http://silktide.com/cookieconsent -->
<script type="text/javascript">
    window.cookieconsent_options = {"message":"This website uses cookies to ensure you get the best experience","dismiss":"Got it!","learnMore":"More info","link":"http://www.gsmarena.com/privacy.php3","theme":"dark-floating"};
</script>

<script type="text/javascript" src="//cdnjs.cloudflare.com/ajax/libs/cookieconsent2/1.0.9/cookieconsent.min.js"></script>
<!-- End Cookie Consent plugin -->


<script data-cfasync="false" type="text/javascript">(function(w, d) { var s = d.createElement('script'); s.src = '//delivery.adrecover.com/16425/adRecover.js'; s.type = 'text/javascript'; s.async = true; (d.getElementsByTagName('head')[0] || d.getElementsByTagName('body')[0]).appendChild(s); })(window, document);</script>
<link rel="stylesheet" href="http://cdn.gsmarena.com/vv/assets9/css/specs.css?v=17">
<link rel="stylesheet" href="http://cdn.gsmarena.com/vv/assets9/css/comments-2.css">

<meta http-equiv=Content-Type content="text/html; charset=iso-8859-1">
<meta name=Description content="Apple iPhone 7 smartphone. Announced 2016, September. Features 3G, 4.7&Prime; LED-backlit IPS LCD display, 12 MP camera, Wi-Fi, GPS, Bluetooth.">
<meta name=keywords content="Apple iPhone 7,Apple,iPhone 7,GSM,mobile,phone,cellphone,information,info,specs,specification,opinion,review">
<link rel="shortcut icon" href="i/favicon.ico" />
<link rel="canonical" href="http://www.gsmarena.com/apple_iphone_7-8064.php">


</head>
<body>

<script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>

<script type="text/javascript" src="http://cdn.gsmarena.com/vv/assets8/js/misc.js?v=18"></script>
<script type="text/javascript" src="http://cdn.gsmarena.com/vv/assets8/js/autocomplete.js?ver=13"></script>
<script type="text/javascript" language="javascript">
AUTOCOMPLETE_LIST_URL = "/quicksearch-8089.jpg";
$gsm.addEventListener(document, "DOMContentLoaded", function() 
{
    new Autocomplete( "topsearch-text", "topsearch", true );
}
)
</script>
<script language='JavaScript' type='text/javascript'>
function phpads_deliverActiveX(content)
{
	document.write(content);	
}
</script>
<header id="header" class="row">
<div class="wrapper clearfix">
<div class="top-bar clearfix">
<!-- HAMBURGER MENU -->
<button type="button" role="button" aria-label="Toggle Navigation" class="lines-button minus focused">
<span class="lines"></span>
</button>
<!-- /HAMBURGER MENU -->



<!-- LOGO -->
<div id="logo">
<a href="/">

<object type="image/svg+xml" data="http://cdn.gsmarena.com/vv/assets9/i/logo.svg"><img src="http://cdn.gsmarena.com/vv/assets9/i/logo-fallback.gif" alt="GSMArena.com"></object>
<span>GSMArena.com</span></a>
</div>



<div id="nav" role="main">
<form action="results.php3" method="get" id="topsearch">
    <input type="hidden" name="sQuickSearch" value="yes">
    <input type="text" placeholder="Search" tabindex="201" accesskey="s" id="topsearch-text" name="sName" autocomplete="off" />
    <span id="quick-search-button">
      <input type="submit" value="Go" />
      <i class="head-icon icomoon-liga icon-search-left"></i>
    </span>
    

</form>
</div>


<div id="social-connect">
<a href="tipus.php3" class="tip-icon">
  <i class="head-icon icon-tip-us icomoon-liga"></i><br><span class="icon-count">Tip us</span>
</a>
<a href="https://www.facebook.com/GSMArenacom-189627474421/" class="fb-icon" target="_blank">
  <i class="head-icon icon-soc-fb2 icomoon-liga"></i><br><span class="icon-count">868k</span>
</a>
<a href="http://twitter.com/gsmarena_com" class="tw-icon" target="_blank">
  <i class="head-icon icon-soc-twitter2 icomoon-liga"></i><br><span class="icon-count">130k</span>
</a>

<a href="https://plus.google.com/116083888509266864115?prsrc=3" class="gp-icon" target="_blank">
  <i class="head-icon icon-soc-gplus icomoon-liga"></i>
  <span class="icon-count">87k</span>
</a>
<a href="https://www.youtube.com/channel/UCbLq9tsbo8peV22VxbDAfXA?sub_confirmation=1" class="yt-icon" target="_blank">
  <i class="head-icon icon-soc-youtube icomoon-liga"></i><br><span class="icon-count">212k</span>
</a>
<a href="rss-news-reviews.php3" class="rss-icon">
  <i class="head-icon icon-soc-rss2 icomoon-liga"></i><br><span class="icon-count">RSS</span>
</a>




	<a href="#" onclick="return false;" class="login-icon" id="login-active">
	  <i class="head-icon icon-login"></i><br><span class="icon-count" style="right:4px;">Log in</span>
	</a>

	<span class="tooltip" id="login-popup">
	   <p>
	     Login with<br />
	     <a href="login-facebook.php3?rdr=MH5vb3N6QHZvd3BxekAoMicvKSsxb3dv"><i class="head-icon icon-soc-fb2"></i>Facebook</a>
	     <a class="g-login" href="login-google.php3?rdr=MH5vb3N6QHZvd3BxekAoMicvKSsxb3dv"><i class="head-icon icon-soc-gplus"></i>Google</a>
	   </p>
	</span>
 <a href="nickname.php3?sSource=MH5vb3N6QHZvd3BxekAoMicvKSsxb3dv" class="signup-icon no-margin-right"><i class="head-icon icon-user-plus"></i><span class="icon-count">Sign up</span></a>  
              </div>  
           </div>                 
<ul id="menu" class="main-menu-list">
<li><a href="/">Home</a></li>
	<li><a href="news.php3">News</a></li>
	<li><a href="reviews.php3">Reviews</a></li>
	<li><a href="https://www.youtube.com/channel/UCbLq9tsbo8peV22VxbDAfXA?sub_confirmation=1" target="_blank">Video</a></li>
	<li><a href="search.php3">Phone Finder</a></li>
	<li><a href="tools.php3">Tools</a></li>
	<li><a href="glossary.php3">Glossary</a></li>
	<li><a href="network-bands.php3">Coverage</a></li>
	<li><a href="faq.php3">FAQ</a></li>
	<li><a href="contact.php3">Contact</a></li>   
                  
      </ul>
      <!-- SOCIAL CONNECT -->
    </div>
    

</header> <!--- HEADER END -->


		
<script type="text/javascript" language="javascript">
HISTORY_ITEM_ID = "8064";
HISTORY_ITEM_NAME = "Apple iPhone 7";
HISTORY_ITEM_URL = "apple_iphone_7-8064.php";
HISTORY_ITEM_IMAGE = "http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-7r4.jpg";

</script>
<div id="wrapper" class="l-container">
<div id="outer" class="row">


<div id="subHeader" class="col">
<div id="topPromo">		
		<div class="alt-display is-review" style="background-image: url(http://cdn.gsmarena.com/imgroot/reviews/17/sony-xperia-xa1/-347x151/gsmarena_000.jpg)">
		  <a class="table-cell reviews-xl-snazzy" href="sony_xperia_xa1-review-1606.php">
			  <div class="module-review-xl-title">
			 
			    	<span>Square one</span><br>
			    	<strong>Sony Xperia XA1 review</strong>
			   
			  
		 	  </div>
		 </a>
	  </div>
</div><div id="topAdv" class="l-box">
<script language='JavaScript' type='text/javascript'>
<!--
   if (!document.phpAds_used) document.phpAds_used = ',';
   phpAds_random = new String (Math.random()); phpAds_random = phpAds_random.substring(2,11);
   
   document.write ("<" + "script language='JavaScript' type='text/javascript' src='");
   document.write ("http://a.gsmarena.com/adjs.php?n=" + phpAds_random);
   document.write ("&amp;what=zone:5&amp;target=_blank");
   document.write ("&amp;exclude=" + document.phpAds_used);
   if (document.referrer)
      document.write ("&amp;referer=" + escape(document.referrer));
   document.write ("'><" + "/script>");
//-->
</script><noscript><a href='http://a.gsmarena.com/adclick.php?n=afad88d6' target='_blank'><img src='http://a.gsmarena.com/adview.php?what=zone:5&amp;n=afad88d6' border='0' alt=''></a></noscript>
</div>   
</div>


<div id="body">

<div class="main main-review right l-box col">  

<div class="review-header hreview">  
    <div class="article-info">
<style type="text/css">
    .review-header::after {
	background-image:url( http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-7r4.jpg );
	background-size: 333%;
	background-position: -932px -2089px;
    }
</style>


        <div class="article-info-line page-specs light border-bottom">
            <div class="blur review-background"></div>
            <h1 class="specs-phone-name-title" data-spec="modelname">Apple iPhone 7</h1>



<script>
	var sURLSocialE = "http%3A%2F%2Fwww.gsmarena.com%2Fapple_iphone_7-8064.php";
</script>


<ul class="social-share sharrre">
<li class="help help-social">
  <a class="box btnFb" title="Facebook" id="facebook" href="http://www.facebook.com/sharer.php?u=http%3A%2F%2Fwww.gsmarena.com%2Fapple_iphone_7-8064.php" target="_blank" onclick="window.open('http://www.facebook.com/sharer.php?u=http%3A%2F%2Fwww.gsmarena.com%2Fapple_iphone_7-8064.php','fbookshare','width=500,height=400,left='+(screen.availWidth/2-225)+',top='+(screen.availHeight/2-150)+'');return false;">
    
    <div class="share">
      <span class="count fbCount" href="#">-</span>
      <i class="head-icon icon-soc-fb2"></i>
    </div>
  </a>
</li>
<li>
  <a class="box btnTw" title="Twitter" id="twitter" href="https://twitter.com/intent/tweet?text=Apple+iPhone+7&url=http%3A%2F%2Fwww.gsmarena.com%2Fapple_iphone_7-8064.php" target="_blank" onclick="window.open('https://twitter.com/intent/tweet?text=Apple+iPhone+7&url=http%3A%2F%2Fwww.gsmarena.com%2Fapple_iphone_7-8064.php','twitshare','width=500,height=400,left='+(screen.availWidth/2-225)+',top='+(screen.availHeight/2-150)+'');return false;">
    <div class="share">
      <span class="count twCount" href="#">-</span>
      <i class="head-icon icon-soc-twitter2"></i></div>
  </a>
</li>
<li>
  <a class="box btnGo" title="Google+" id="googleplus" href="https://plusone.google.com/_/+1/confirm?hl=en&url=http%3A%2F%2Fwww.gsmarena.com%2Fapple_iphone_7-8064.php" target="_blank" onclick="window.open('https://plus.google.com/share?url=http%3A%2F%2Fwww.gsmarena.com%2Fapple_iphone_7-8064.php','gplusshare','width=500,height=400,left='+(screen.availWidth/2-225)+',top='+(screen.availHeight/2-150)+'');return false;">
    
    <div class="share">
      <span class="count goCount" href="#">-</span>
      <i class="head-icon icon-soc-gplus"></i>
    </div>
  </a>
</li>
</ul>             


        </div>




        

<div class="center-stage light nobg specs-accent">
  <div class="specs-photo-main">
<a href=apple_iphone_7-pictures-8064.php><img alt="Apple iPhone 7
MORE PICTURES" src=http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-7r4.jpg></a>      
  </div>
  <ul class="specs-spotlight-features" style="overflow:hidden;">
    <li class="specs-brief pattern">
      <span class="specs-brief-accent"><i class="head-icon icon-launched"></i><span data-spec="released-hl">Released 2016, September</span></span><br>
      <span class="specs-brief-accent"><i class="head-icon icon-mobile2"></i><span data-spec="body-hl">138g, 7.1mm thickness</span></span><br>
      <span class="specs-brief-accent"><i class="head-icon icon-os"></i><span data-spec="os-hl">iOS 10.0.1, up to iOS 10.3.2</span></span><br>
      <span class="specs-brief-accent"><i class="head-icon icon-sd-card-0"></i><span data-spec="storage-hl">32/128/256GB storage, no card slot</span></span>  
      
      <span class="help help-quickfacts"></span>
    </li>
    
    <li class="light pattern help help-popularity">
     
      <strong class="accent"> <i class="head-icon icon-popularity"></i>28%</strong>
      <span>20,862,149 hits</span></li>
    <li class="light pattern help help-fans">
      <a class="specs-fans" href="">
        <strong class="accent"><i class="head-icon icon-fans"></i>609</strong>
        <span>Become a fan</span>
      </a>
    </li>
    <li class="help accented help-display">
      <i class="head-icon icon-touch-1"></i>
      <strong class="accent">4.7"</strong><div data-spec="displayres-hl">750x1334 pixels</div>
    </li>
    <li class="help accented help-camera">
      <i class="head-icon icon-camera-1"></i>
      <strong class="accent accent-camera"><span data-spec="camerapixels-hl">12</span><span>MP</span>
      </strong> <div data-spec="videopixels-hl">2160p</div></li>
    <li class="help accented help-expansion">
      <i class="head-icon icon-cpu"></i>
      <strong class="accent accent-expansion"><span data-spec="ramsize-hl">2</span><span>GB RAM</span></strong> 
      <div data-spec="chipset-hl">Apple A10 Fusion</div></li>


    <li class="help accented help-battery">
    <i class="head-icon icon-battery-1"></i>
    
    <strong class="accent accent-battery"><span data-spec="batsize-hl">1960</span><span>mAh</span></strong><div data-spec="battype-hl">Li-Ion</div></li>
    
  </ul>
</div>

<div class="article-info-line page-specs light">

<ul class="article-info-meta">

<li class="article-info-meta-link article-info-meta-link-review light large help help-review has-short"><a href="apple_iphone_7-review-1497.php"><i class="head-icon icon-review"></i>Review</a><a href="apple_iphone_7_time_saver-review-1524.php" class="help help-small-review"><i class="head-icon icon-stopwatch" title="Short review"></i></a></li><li class="article-info-meta-link light"><a href=apple_iphone_7-3d-spin-8064.php><i class="head-icon icon-360-view"></i>360&deg; view</a></li>

<li class="article-info-meta-link light"><a href=apple_iphone_7-pictures-8064.php><i class="head-icon icon-pictures"></i>Pictures</a></li>
<li class="article-info-meta-link light"><a href=compare.php3?idPhone1=8064><i class="head-icon icon-mobile-phone231 icon-compare"></i>Compare</a></li>
<li class="article-info-meta-link light" title="Apple iPhone 7 user reviews and opinions"><a href="apple_iphone_7-reviews-8064.php"><i class="head-icon icon-comment-count"></i>Opinions</a></li>


<br style="clear:both;" />
</ul>
</div>

</div> 			
</div>




<script>
var SPEC_VERSIONS = [[
["a1660", {
"nettech": "GSM \/ HSPA \/ LTE",
"net2g": "GSM 850 \/ 900 \/ 1800 \/ 1900 & CDMA2000 1xEV-DO; TD-SCDMA",
"net3g": "HSDPA 850 \/ 900 \/ 1700(AWS) \/ 1900 \/ 2100 ",
"net3g": "HSDPA 850 \/ 900 \/ 1700(AWS) \/ 1900 \/ 2100 ",
"net4g": "LTE band 1(2100), 2(1900), 3(1800), 4(1700\/2100), 5(850), 7(2600), 8(900), 12(700), 13(700), 17(700), 18(800), 19(800), 20(800), 25(1900), 26(850), 27(800), 28(700), 29(700), 30(2300), 38(2600), 39(1900), 40(2300), 41(2500)",
"sar-us": "1.19 W\/kg (head) &nbsp; &nbsp; 1.19 W\/kg (body) &nbsp; &nbsp; ",
"sar-us": "1.19 W\/kg (head) &nbsp; &nbsp; 1.19 W\/kg (body) &nbsp; &nbsp; ",
"sar-eu": "",
"sar-eu": "",
"comment": "For USA & China",
}],
["a1778", {
"nettech": "GSM \/ HSPA \/ LTE",
"net2g": "GSM 850 \/ 900 \/ 1800 \/ 1900 ",
"net3g": "HSDPA 850 \/ 900 \/ 1700(AWS) \/ 1900 \/ 2100 ",
"net3g": "HSDPA 850 \/ 900 \/ 1700(AWS) \/ 1900 \/ 2100 ",
"net4g": "LTE band 1(2100), 2(1900), 3(1800), 4(1700\/2100), 5(850), 7(2600), 8(900), 12(700), 13(700), 17(700), 18(800), 19(800), 20(800), 25(1900), 26(850), 27(800), 28(700), 29(700), 30(2300), 38(2600), 39(1900), 40(2300), 41(2500)",
"sar-us": "",
"sar-us": "",
"sar-eu": "1.38 W\/kg (head) &nbsp; &nbsp; 1.34 W\/kg (body) &nbsp; &nbsp; ",
"sar-eu": "1.38 W\/kg (head) &nbsp; &nbsp; 1.34 W\/kg (body) &nbsp; &nbsp; ",
"comment": "For Global market",
}],
]];
</script>


<script language="JavaScript">
<!--
function helpW( strURL )
{
window.open( 'help.php3?term=' + strURL, '_blank', 'toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=no,width=420,height=390' );
}
//-->
</script>

<div id="specs-list">






<div class="specs-tabs">
<div class="swiper-wrapper">
<h2 class="tab active" data-version="*">ALL VERSIONS</h2>
<h2 class="tab" data-version="a1660">A1660</h2><h2 class="tab" data-version="a1778">A1778</h2></div>
</div>


					
<style type="text/css"> .tr-toggle {  display:none; }  </style>


<table cellspacing="0">
<tr class="tr-hover">
<th rowspan="15" scope="row">Network</th>
<td class="ttl"><a href="network-bands.php3">Technology</a></td>
<td class="nfo"><a href="#" class="link-network-detail collapse" data-spec="nettech">GSM / CDMA / HSPA / EVDO / LTE</a></td>
</tr>
<tr class="tr-toggle">
<td class="ttl"><a href="network-bands.php3">2G bands</a></td>
<td class="nfo" data-spec="net2g">GSM 850 / 900 / 1800 / 1900 - A1660, A1778</td>
</tr><tr class="tr-toggle" data-spec-optional>
<td class="ttl">&nbsp;</td>
<td class="nfo">CDMA 800 / 1900 / 2100 - A1660</td>
</tr>
<tr class="tr-toggle">
<td class="ttl"><a href="network-bands.php3">3G bands</a></td>
<td class="nfo" data-spec="net3g">HSDPA 850 / 900 / 1700(AWS) / 1900 / 2100 - A1660, A1778</td>
</tr>
<tr class="tr-toggle" data-spec-optional>
<td class="ttl">&nbsp;</td>
<td class="nfo">CDMA2000 1xEV-DO & TD-SCDMA - A1660</td>
</tr>
<tr class="tr-toggle">
<td class="ttl"><a href="network-bands.php3">4G bands</a></td>
<td class="nfo" data-spec="net4g">LTE band 1(2100), 2(1900), 3(1800), 4(1700/2100), 5(850), 7(2600), 8(900), 12(700), 13(700), 17(700), 18(800), 19(800), 20(800), 25(1900), 26(850), 27(800), 28(700), 29(700), 30(2300), 38(2600), 39(1900), 40(2300), 41(2500) - A1660, A1778</td>
</tr>
<tr class="tr-toggle">
<td class="ttl"><a href="glossary.php3?term=3g">Speed</a></td>
<td class="nfo" data-spec="speed">HSPA 42.2/5.76 Mbps, LTE-A (3CA) Cat9 450/50 Mbps, EV-DO Rev.A 3.1 Mbps</td>
</tr>
	
<tr class="tr-toggle">
<td class="ttl"><a href="glossary.php3?term=gprs">GPRS</a></td>
<td class="nfo" data-spec="gprstext">Yes</td>
</tr>	
<tr class="tr-toggle">
<td class="ttl"><a href="glossary.php3?term=edge">EDGE</a></td>
<td class="nfo" data-spec="edge">Yes</td>
</tr>
</table>


<table cellspacing="0">
<tr>
<th rowspan="2" scope="row">Launch</th>
<td class="ttl"><a href=# onClick="helpW('h_year.htm');">Announced</a></td>
<td class="nfo" data-spec="year">2016, September</td>
</tr>	
<tr>
<td class="ttl"><a href=# onClick="helpW('h_status.htm');">Status</a></td>
<td class="nfo" data-spec="status">Available. Released 2016, September</td>
</tr>
</table>


<table cellspacing="0">
<tr>
<th rowspan="6" scope="row">Body</th>
<td class="ttl"><a href=# onClick="helpW('h_dimens.htm');">Dimensions</a></td>
<td class="nfo" data-spec="dimensions">138.3 x 67.1 x 7.1 mm (5.44 x 2.64 x 0.28 in)</td>
</tr><tr>
<td class="ttl"><a href=# onClick="helpW('h_weight.htm');">Weight</a></td>
<td class="nfo" data-spec="weight">138 g (4.87 oz)</td>
</tr>
<tr>
<td class="ttl"><a href="glossary.php3?term=sim">SIM</a></td>
<td class="nfo" data-spec="sim">Nano-SIM</td>
</tr>
<tr><td class="ttl">&nbsp;</td><td class="nfo" data-spec="bodyother">- IP67 certified - dust and water resistant<br />
- Water resistant up to 1 meter and 30 minutes<br />
- Apple Pay (Visa, MasterCard, AMEX certified)</td></tr>
		
</table>


<table cellspacing="0">
<tr>
<th rowspan="6" scope="row">Display</th>
<td class="ttl"><a href="glossary.php3?term=display-type">Type</a></td>
<td class="nfo" data-spec="displaytype">LED-backlit IPS LCD, capacitive touchscreen, 16M colors</td>
</tr>
<tr>
<td class="ttl"><a href=# onClick="helpW('h_dsize.htm');">Size</a></td>
<td class="nfo">4.7 inches (~65.6% screen-to-body ratio)</td>
</tr>
<tr>
<td class="ttl"><a href=# onClick="helpW('h_dres.htm');">Resolution</a></td>
<td class="nfo" data-spec="displayresolution">750 x 1334 pixels (~326 ppi pixel density)</td>
</tr>
<tr>
<td class="ttl"><a href="glossary.php3?term=multitouch">Multitouch</a></td>
<td class="nfo">Yes</td>
</tr>
<tr>
<td class="ttl"><a href="glossary.php3?term=screen-protection">Protection</a></td>
<td class="nfo" data-spec="displayprotection">Ion-strengthened glass, oleophobic coating</td>
</tr>
<tr><td class="ttl">&nbsp;</td><td class="nfo" data-spec="displayother">- Wide color gamut display<br />
- 3D Touch display & home button<br />
- Display Zoom</td></tr>
		
</table>


<table cellspacing="0">
<tr>
<th rowspan="4" scope="row">Platform</th>
<td class="ttl"><a href="glossary.php3?term=os">OS</a></td>
<td class="nfo" data-spec="os">iOS 10.0.1, upgradable to iOS 10.3.2</td>
</tr>
<tr><td class="ttl"><a href="glossary.php3?term=chipset">Chipset</a></td>
<td class="nfo" data-spec="chipset">Apple A10 Fusion</td>
</tr>
<tr><td class="ttl"><a href="glossary.php3?term=cpu">CPU</a></td>
<td class="nfo" data-spec="cpu">Quad-core 2.34 GHz (2x Hurricane + 2x Zephyr)</td>
</tr>
<tr><td class="ttl"><a href="glossary.php3?term=gpu">GPU</a></td>
<td class="nfo" data-spec="gpu">PowerVR Series7XT Plus (six-core graphics)</td>
</tr>
</table>


<table cellspacing="0">
<tr>
<th rowspan="5" scope="row">Memory</th>
<td class="ttl"><a href="glossary.php3?term=memory-card-slot">Card slot</a></td>


<td class="nfo" data-spec="memoryslot">No</td></tr>

	

<tr>
<td class="ttl"><a href="glossary.php3?term=dynamic-memory">Internal</a></td>
<td class="nfo" data-spec="internalmemory">32/128/256 GB, GB, 2 GB RAM</td>
</tr>
	

			
</td>
</tr>
</table>


<table cellspacing="0">
<tr>
<th rowspan="4" scope="row">Camera</th>
<td class="ttl"><a href="glossary.php3?term=camera">Primary</a></td>
<td class="nfo" data-spec="cameraprimary">12 MP, f/1.8, 28mm, phase detection autofocus, OIS, quad-LED (dual tone) flash, <a href="piccmp.php3?idType=1&idPhone1=8064&nSuggest=1">check quality</a></td>
</tr>
<tr>
<td class="ttl"><a href="glossary.php3?term=camera">Features</a></td>
<td class="nfo" data-spec="camerafeatures">1/3" sensor size, geo-tagging, simultaneous 4K video and 8MP image recording, touch focus, face/smile detection, HDR (photo/panorama)</td>
</tr>
<tr>
<td class="ttl"><a href="glossary.php3?term=camera">Video</a></td>
<td class="nfo" data-spec="cameravideo">2160p@30fps, 1080p@30/60/120fps, 720p@240fps, <a href="vidcmp.php3?idType=3&idPhone1=8064&nSuggest=1">check quality</a></td>
</tr>
<tr>
<td class="ttl"><a href="glossary.php3?term=video-call">Secondary</a></td>
<td class="nfo" data-spec="camerasecondary">7 MP, f/2.2, 32mm, 1080p@30fps, 720p@240fps, face detection, HDR, panorama</td>
</tr>
</table>


<table cellspacing="0">
<tr>
<th rowspan="4" scope="row">Sound</th>
<td class="ttl"><a href="glossary.php3?term=call-alerts">Alert types</a></td>
<td class="nfo">Vibration, proprietary ringtones</td>
	</tr>
	
<tr>
<td class="ttl"><a href="glossary.php3?term=loudspeaker">Loudspeaker</a> </td>
<td class="nfo">Yes, with stereo speakers</td>
</tr>

<tr>
<td class="ttl"><a href="glossary.php3?term=audio-jack">3.5mm jack</a> </td>
<td class="nfo">No</td>
</tr>
	

<tr><td class="ttl">&nbsp;</td><td class="nfo" data-spec="optionalother">- Active noise cancellation with dedicated mic<br />
- Lightning to 3.5 mm headphone jack adapter incl.</td></tr>
	
</table>


<table cellspacing="0">
<tr>
<th rowspan="9" scope="row">Comms</th>
<td class="ttl"><a href="glossary.php3?term=wi-fi">WLAN</a></td>
<td class="nfo" data-spec="wlan">Wi-Fi 802.11 a/b/g/n/ac, dual-band, hotspot</td>
</tr>
<tr>
<td class="ttl"><a href="glossary.php3?term=bluetooth">Bluetooth</a></td>
<td class="nfo" data-spec="bluetooth">4.2, A2DP, LE</td>
</tr>
<tr>
<td class="ttl"><a href="glossary.php3?term=gps">GPS</a></td>
<td class="nfo" data-spec="gps">Yes, with A-GPS, GLONASS</td>
</tr>  
<tr>
<td class="ttl"><a href="glossary.php3?term=nfc">NFC</a></td>
<td class="nfo" data-spec="nfc">Yes (Apple Pay only)</td>
</tr>
	
	
<tr>
<td class="ttl"><a href="glossary.php3?term=fm-radio">Radio</a></td>
<td class="nfo" data-spec="radio">No</td>
</tr>
   
<tr>
<td class="ttl"><a href="glossary.php3?term=usb">USB</a></td>
<td class="nfo" data-spec="usb">2.0, reversible connector</td>
</tr>
</table>


<table cellspacing="0">
<tr>
<th rowspan="12" scope="row">Features</th>
<td class="ttl"><a href="glossary.php3?term=sensors">Sensors</a></td>
<td class="nfo" data-spec="sensors">Fingerprint (front-mounted), accelerometer, gyro, proximity, compass, barometer</td>
</tr><tr>
<td class="ttl"><a href="glossary.php3?term=messaging">Messaging</a></td>
<td class="nfo">iMessage, SMS (threaded view), MMS, Email, Push Email</td>
</tr><tr>
<td class="ttl"><a href="glossary.php3?term=browser">Browser</a></td>
<td class="nfo">HTML5 (Safari)</td>
</tr> 	

 	
<tr>
<td class="ttl"><a href="glossary.php3?term=java">Java</a></td>
<td class="nfo">No</td>
</tr>
<tr><td class="ttl">&nbsp;</td><td class="nfo" data-spec="featuresother">- Siri natural language commands and dictation<br />
- iCloud cloud service<br />
- MP3/WAV/AAX+/AIFF/Apple Lossless player<br />
- MP4/H.264 player<br />
- Audio/video/photo editor<br />
- Document editor</td></tr>
	
</table>


<table cellspacing="0">
<tr>
<th rowspan="7" scope="row">Battery</th>
<td class="ttl">&nbsp;</td>
<td class="nfo" data-spec="batdescription1">Non-removable Li-Ion 1960 mAh battery (7.45 Wh)</td>
</tr>

<tr>
<td class="ttl"><a href="glossary.php3?term=talk-time">Talk time</a></td>
<td class="nfo" data-spec="battalktime1">Up to 14 h (3G)</td>
</tr>

<tr>
<td class="ttl"><a href="glossary.php3?term=music-playback-time">Music play</a></td>
<td class="nfo" data-spec="batmusicplayback1">Up to 40 h</td>
</tr>
</table>


<table cellspacing="0">
<tr>
<th rowspan="5" scope="row">Misc</th>
<td class="ttl"><a href=# onClick="helpW('h_colors.htm');">Colors</a></td>
<td class="nfo" data-spec="colors">Jet Black, Black, Silver, Gold, Rose Gold, Red</td>
</tr>
<tr>
<td class="ttl"><a href="glossary.php3?term=sar">SAR</a></td>
<td class="nfo" data-spec="sar-us">1.19 W/kg (head) &nbsp; &nbsp; 1.19 W/kg (body) &nbsp; &nbsp; </td>
</tr>
<tr>
<td class="ttl"><a href="glossary.php3?term=sar">SAR EU</a></td>
<td class="nfo" data-spec="sar-eu">1.38 W/kg (head) &nbsp; &nbsp; 1.34 W/kg (body) &nbsp; &nbsp; </td>
</tr>


<tr>
<td class="ttl"><a href=# onClick="helpW('h_price.htm');">Price</a></td>
<td class="nfo" data-spec="price">About 760 EUR</td>
</tr>
</table>


<table cellspacing="0">
<tr>
<th rowspan="6" scope="row">Tests</th>
<td class="ttl"><a href="glossary.php3?term=benchmarking">Performance</a></td>
<td class="nfo" data-spec="tbench">
<a class="noUnd" href="benchmark-test.php3?idPhone=8064#show">Basemark OS II 2.0: 3416</a></td>
</tr><tr>

<td class="ttl"><a href="gsmarena_lab_tests-review-751p2.php">Display</a></td>
<td class="nfo">
<a class="noUnd" href="http://www.gsmarena.com/apple_iphone_7-review-1497p3.php#dt">Contrast ratio: 1603:1 (nominal), 3.964 (sunlight)</a></td>
</tr><tr>

<td class="ttl"><a href="gsmarena_lab_tests-review-751p5.php">Camera</a></td>
<td class="nfo">
<a class="noUnd" href="piccmp.php3?idType=1&idPhone1=8064&nSuggest=1">Photo</a> / <a class="noUnd" href="vidcmp.php3?idType=3&idPhone1=8064&nSuggest=1">Video</a></td>
</tr><tr>

<td class="ttl"><a href="gsmarena_lab_tests-review-751p3.php">Loudspeaker</a></td>
<td class="nfo">
<a class="noUnd" href="http://www.gsmarena.com/apple_iphone_7-review-1497p6.php#lt">Voice 67dB / Noise 73dB / Ring 75dB</a>

</td>
</tr><tr>

<td class="ttl"><a href="gsmarena_lab_tests-review-751p4.php">Audio quality</a></td>
<td class="nfo">
<a class="noUnd" href="http://www.gsmarena.com/apple_iphone_7-review-1497p6.php#aq">Noise -92.4dB / Crosstalk -80.9dB</a></td>
</tr><tr>


<td class="ttl"><a href="gsmarena_lab_tests-review-751p6.php">Battery life</a></td>
<td class="nfo" data-spec="batlife">
<div style="position:relative;">
<a href="#" onclick="showBatteryPopup(event, 8064); ">Endurance rating 61h</a><div class="popover top" id="battery-popover" style="display: none;"></div>
</div>
</td>
</tr><tr>

</tr></table>



</div>




<p class="note"><strong>Disclaimer.</strong> We can not guarantee that the information on this page is 100% correct. <a href=# onClick="helpW('legal.htm');">Read more</a></p>


<div class="article-info-line page-specs light">

<ul class="article-info-meta">

<li class="article-info-meta-link article-info-meta-link-review light large help help-review has-short"><a href="apple_iphone_7-review-1497.php"><i class="head-icon icon-review"></i>Review</a><a href="apple_iphone_7_time_saver-review-1524.php" class="help help-small-review"><i class="head-icon icon-stopwatch" title="Short review"></i></a></li><li class="article-info-meta-link light"><a href=apple_iphone_7-3d-spin-8064.php><i class="head-icon icon-360-view"></i>360&deg; view</a></li>

<li class="article-info-meta-link light"><a href=apple_iphone_7-pictures-8064.php><i class="head-icon icon-pictures"></i>Pictures</a></li>
<li class="article-info-meta-link light"><a href=compare.php3?idPhone1=8064><i class="head-icon icon-mobile-phone231 icon-compare"></i>Compare</a></li>
<li class="article-info-meta-link light" title="Apple iPhone 7 user reviews and opinions"><a href="apple_iphone_7-reviews-8064.php"><i class="head-icon icon-comment-count"></i>Opinions</a></li>


<br style="clear:both;" />
</ul>
</div>

<div style="margin-top: 10px;"></div>
					
<div id="user-comments" class="box s3 nobg">
<h2><a href="apple_iphone_7-reviews-8064.php">Apple iPhone 7 - user opinions and reviews</a></h2>
						
<div class="user-thread">
<div class="uavatar"><i class="head-icon icon-user"></i></div>
<ul class="uinfo2">
<li class="uname2">Anonymous</li>
<li class="ulocation">
<i class="head-icon icon-location"></i>
<span title="Encoded location">6XUu</span></li>
<li class="upost"><time>13 Jun 2017</time></li>
</ul>
<p class="uopin">I agree. But some people prefer small phone instead of phablet.</p>

<ul class="uinfo">
<li class="ureply">
<span title="Reply to this post">
<a href="postopinion.php3?idPhone=8064&idOpinion=5639812">Reply</a></span>
</li>


</ul>




</div>
						
<div class="user-thread">
<div class="uavatar"><i class="head-icon icon-user"></i></div>
<ul class="uinfo2">
<li class="uname"><b>AdelJ</b></li>
<li class="ulocation">
<i class="head-icon icon-location"></i>
<span title="Encoded location">gya$</span></li>
<li class="upost"><time>13 Jun 2017</time></li>
</ul>
<p class="uopin">The best iPhone is the iPhone 7 Plus period.</p>

<ul class="uinfo">
<li class="ureply">
<span title="Reply to this post">
<a href="postopinion.php3?idPhone=8064&idOpinion=5639790">Reply</a></span>
</li>


</ul>




</div>
						
<div class="user-thread">
<div class="uavatar"><i class="head-icon icon-user"></i></div>
<ul class="uinfo2">
<li class="uname2">Msk</li>
<li class="ulocation">
<i class="head-icon icon-location"></i>
<span title="Encoded location">f3h7</span></li>
<li class="upost"><time>13 Jun 2017</time></li>
</ul>
<p class="uopin">I would suggest wait and get the iphone 7 would be a great upgrade for you from an iphone user perspective</p>

<ul class="uinfo">
<li class="ureply">
<span title="Reply to this post">
<a href="postopinion.php3?idPhone=8064&idOpinion=5639583">Reply</a></span>
</li>


</ul>




</div>
		
<div class="sub-footer">
<div class="button-links">
<ul>
								
<li><a class="button" href="apple_iphone_7-reviews-8064.php">Read all opinions</a></li>
<li><a class="button" href="postopinion.php3?idPhone=8064">Post your opinion</a></li>
</ul>

</div>
<div id="opinions-total">Total user opinions: <b>3272</b></div>
<br class="clear" />
									
						</div>
			


<div class="adv bottom-728">
<script type="text/javascript"><!--
google_ad_client = "ca-pub-4873060236139130";
/* Main 728 BTF */
google_ad_slot = "8399841746";
google_ad_width = 728;
google_ad_height = 200;
//-->
</script>
<script type="text/javascript"
src="//pagead2.googlesyndication.com/pagead/show_ads.js">
</script>
</div>



			


</div>
</div>

<aside class="sidebar col left">

<div class="brandmenu-v2 light l-box clearfix">
<p class="pad">
<a href="search.php3" class="pad-single pad-finder">
<i class="head-icon icon-search-right"></i>
<span>Phone finder</span></a>
</p>
<ul>
<li><a href="samsung-phones-9.php">Samsung</a></li><li><a href="apple-phones-48.php">Apple</a></li><li><a href="microsoft-phones-64.php">Microsoft</a></li><li><a href="nokia-phones-1.php">Nokia</a></li><li><a href="sony-phones-7.php">Sony</a></li><li><a href="lg-phones-20.php">LG</a></li><li><a href="htc-phones-45.php">HTC</a></li><li><a href="motorola-phones-4.php">Motorola</a></li><li><a href="huawei-phones-58.php">Huawei</a></li><li><a href="lenovo-phones-73.php">Lenovo</a></li><li><a href="xiaomi-phones-80.php">Xiaomi</a></li><li><a href="google-phones-107.php">Google</a></li><li><a href="acer-phones-59.php">Acer</a></li><li><a href="asus-phones-46.php">Asus</a></li><li><a href="oppo-phones-82.php">Oppo</a></li><li><a href="oneplus-phones-95.php">OnePlus</a></li><li><a href="meizu-phones-74.php">Meizu</a></li><li><a href="blackberry-phones-36.php">BlackBerry</a></li><li><a href="alcatel-phones-5.php">Alcatel</a></li><li><a href="zte-phones-62.php">ZTE</a></li><li><a href="toshiba-phones-44.php">Toshiba</a></li><li><a href="vodafone-phones-53.php">Vodafone</a></li><li><a href="gigabyte-phones-47.php">Gigabyte</a></li><li><a href="xolo-phones-85.php">XOLO</a></li><li><a href="lava-phones-94.php">Lava</a></li><li><a href="micromax-phones-66.php">Micromax</a></li><li><a href="blu-phones-67.php">BLU</a></li><li><a href="gionee-phones-92.php">Gionee</a></li><li><a href="vivo-phones-98.php">vivo</a></li><li><a href="leeco-phones-109.php">LeEco</a></li><li><a href="panasonic-phones-6.php">Panasonic</a></li><li><a href="hp-phones-41.php">HP</a></li><li><a href="yu-phones-100.php">YU</a></li><li><a href="verykool-phones-70.php">verykool</a></li><li><a href="maxwest-phones-87.php">Maxwest</a></li><li><a href="plum-phones-72.php">Plum</a></li></ul>

<p class="pad">
<a href="makers.php3" class="pad-multiple pad-allbrands">
  <i class="head-icon icon-mobile-phone231"></i>
  <span>All brands</span>
</a>
<a href="rumored.php3" class="pad-multiple pad-rumormill">
  <i class="head-icon icon-rumored"></i>
  <span>Rumor mill</span>
</a>
</p>
</div>
<div class="adv banner-mpu">

<script language='JavaScript' type='text/javascript'>
<!--
   if (!document.phpAds_used) document.phpAds_used = ',';
   phpAds_random = new String (Math.random()); phpAds_random = phpAds_random.substring(2,11);
   
   document.write ("<" + "script language='JavaScript' type='text/javascript' src='");
   document.write ("http://a.gsmarena.com/adjs.php?n=" + phpAds_random);
   document.write ("&amp;what=zone:156&amp;target=_blank");
   document.write ("&amp;exclude=" + document.phpAds_used);
   if (document.referrer)
      document.write ("&amp;referer=" + escape(document.referrer));
   document.write ("'><" + "/script>");
//-->
</script><noscript><a href='http://a.gsmarena.com/adclick.php?n=afad88d6' target='_blank'><img src='http://a.gsmarena.com/adview.php?what=zone:5&amp;n=afad88d6' border='0' alt=''></a></noscript>
</div>


<div class="module module-phones module-more-promo">
<h4 class="section-heading">More</h4>
<ul>
	

	
<li class="in-the-news-list"><strong><a href="news.php3?idPhoneSearch=8064">In the news</a></strong></li>
	

	
<li class="buy-from-amazon"><strong><a href="https://www.amazon.co.uk/MODEL-APPLE-IPHONE-SIM-Free-BLACK/dp/B01LYUJB5B?psc=1&SubscriptionId=AKIAJKHFFBJUI2OBTOUA&tag=gsmcom-21&linkCode=xm2&camp=2025&creative=165953&creativeASIN=B01LYUJB5B" target=_blank>Buy from Amazon UK</a></strong></li>
	


</ul>
</div>

	  

<style type="text/css">
.checkprice-list::before {
    background: url('http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-7r4.jpg') no-repeat center center;
  }
</style>


<style type="text/css">
	.checkprice-list::before {
	background-size: 333% !important;
	background-position:  -384px -861px;
	}
</style>

<div class="module module-phones module-checkprice">
<h4 class="section-heading">Check Price</h4>
<ul class="checkprice-list">
<li><a href=http://a.gsmarena.com/adclick.php?bannerid=60&zoneid=9&source=&dest=http%3A%2F%2Fwelectronics.com%2Fgsm%2Fapple%2FIphone-7-32GB-gen.HTML target=_blank><i class="head-icon icon-cart"></i>WElectronics</a></li><li><a href=http://a.gsmarena.com/adclick.php?bannerid=118&zoneid=9&source=&dest=https%3A%2F%2Fwww.popularelectronics.com%2Fcollections%2Fapple-unlocked-gsm-smartphone%2Fproducts%2Fapple-iphone-7-4g-lte-unlocked-gsm-smartphone%3Fvariant%3D32019430156 target=_blank><i class="head-icon icon-cart"></i>Popular Electronics</a></li></ul>
</div>
	  
                



<div class="module reviews-xl-snazzy">
<h4 class="section-heading">Apple iPhone 7 reviews</h4>

<a href="apple_iphone_7_time_saver-review-1524.php" class="module-reviews-xl-link">
  <img class="module-reviews-xl-thumb" src="http://cdn.gsmarena.com/imgroot/reviews/16/apple-iphone-7/-347x151/thumb3.jpg" alt="Apple iPhone 7 review: Time-saver edition">
  <div class="module-review-xl-title">
    <span>Time-saver edition</span><br>
    <strong>Apple iPhone 7 review</strong>
  </div>
</a>
<a href="apple_iphone_7-review-1497.php" class="module-reviews-xl-link">
  <img class="module-reviews-xl-thumb" src="http://cdn.gsmarena.com/imgroot/reviews/16/apple-iphone-7/-347x151/thumb4.jpg" alt="Apple iPhone 7 review: Jacked up">
  <div class="module-review-xl-title">
    <span>Jacked up</span><br>
    <strong>Apple iPhone 7 review</strong>
  </div>
</a>
<a href="camera_shootout_iphone7_galaxy_s7_xperia_xz_lg_g5-review-1509.php" class="module-reviews-xl-link">
  <img class="module-reviews-xl-thumb" src="http://cdn.gsmarena.com/imgroot/reviews/16/shootout-g5-iphone7-s7-xz/-347x151/gsmarena_000.jpg" alt="Our camera shootout: iPhone 7 vs. Galaxy S7 vs. Xperia XZ vs. LG G5">
  <div class="module-review-xl-title">
    <span>Our camera shootout</span><br>
    <strong>iPhone 7 vs Galaxy S7 vs Xperia XZ vs LG G5</strong>
  </div>
</a>

</div>
	
<div class="module">


<script type="text/javascript" src='http://adn.ebay.com/files/js/min/ebay_activeContent-min.js'></script>
<script charset="utf-8" type="text/javascript">
document.write('\x3Cscript type="text/javascript" charset="utf-8" src="http://adn.ebay.com/cb?programId=11&campId=5336676177&toolId=10026&customId=sky&keyword=Apple+iPhone+7&minPrice=50&width=300&height=308&font=1&textColor=333366&linkColor=333333&arrowColor=FFAF5E&color1=63769A&color2=[COLORTWO]&format=ImageLink&contentType=TEXT_AND_IMAGE&enableSearch=y&usePopularSearches=n&freeShipping=n&topRatedSeller=n&itemsWithPayPal=n&descriptionSearch=n&showKwCatLink=n&excludeCatId=&excludeKeyword=&catId=15032&disWithin=200&ctx=n&autoscroll=n&flashEnabled=' + isFlashEnabled + '&pageTitle=' + _epn__pageTitle + '&cachebuster=' + (Math.floor(Math.random() * 10000000 )) + '">\x3C/script>' );
</script>

</div>


				
<div class="module module-phones module-related">				
<h4 class="section-heading"><a href="related.php3?idPhone=8064">Related devices</a></h4>

<ul class="clearfix">
<li><a class="module-phones-link" href="apple_iphone_6s-7242.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-6s1.jpg" alt="Phone" /><br>Apple iPhone 6s</a></li><li><a class="module-phones-link" href="apple_iphone_7_plus-8065.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-7-plus-r2.jpg" alt="Phone" /><br>Apple iPhone 7 Plus</a></li><li><a class="module-phones-link" href="samsung_galaxy_s8-8161.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s8-.jpg" alt="Phone" /><br>Samsung Galaxy S8</a></li><li><a class="module-phones-link" href="apple_iphone_6-6378.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-6-4.jpg" alt="Phone" /><br>Apple iPhone 6</a></li><li><a class="module-phones-link" href="apple_iphone_se-7969.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-5se-ofic.jpg" alt="Phone" /><br>Apple iPhone SE</a></li><li><a class="module-phones-link" href="samsung_galaxy_s7-7821.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s7--.jpg" alt="Phone" /><br>Samsung Galaxy S7</a></li>					
</ul>
<p class="more"><a class="more-news-link" href="related.php3?idPhone=8064">More related devices</a></p>					
</div>

				
	<div class="module module-phones module-related phonelist">				
	<h4 class="section-heading"><a href=apple-phones-48.php>Popular from Apple</a></h4>

	<ul class="clearfix">
	<li><a class="module-phones-link" href="apple_iphone_6-6378.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-6-4.jpg" alt="Phone" /><br>Apple iPhone 6</a></li><li><a class="module-phones-link" href="apple_iphone_7-8064.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-7r4.jpg" alt="Phone" /><br>Apple iPhone 7</a></li><li><a class="module-phones-link" href="apple_iphone_5s-5685.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-5s-ofic.jpg" alt="Phone" /><br>Apple iPhone 5s</a></li><li><a class="module-phones-link" href="apple_iphone_7_plus-8065.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-7-plus-r2.jpg" alt="Phone" /><br>Apple iPhone 7 Plus</a></li><li><a class="module-phones-link" href="apple_iphone_6s-7242.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-6s1.jpg" alt="Phone" /><br>Apple iPhone 6s</a></li><li><a class="module-phones-link" href="apple_iphone_se-7969.php"><img src="http://cdn2.gsmarena.com/vv/bigpic/apple-iphone-5se-ofic.jpg" alt="Phone" /><br>Apple iPhone SE</a></li>					
	</ul>
						
	<p class="more"><a class="more-news-link" href="apple-phones-48.php">More from Apple</a></p>	</div>


</aside>

</div><!-- id body -->
</div><!-- id outer -->


<script type="text/javascript" src="http://cdn.gsmarena.com/vv/assets8/js/specs2.js?v=21"></script>
<div id="footer">
 <div class="footer-logo">
     <img src="http://cdn2.gsmarena.com/w/css/logo-gsmarena-com.gif" alt="" />
    </div>
    <div id="footmenu">
<p>
<a href="/">Home</a>
<a href="news.php3">News</a>
<a href="reviews.php3">Reviews</a>
<a href="compare.php3">Compare</a>
<a href="network-bands.php3">Coverage</a>
<a href="glossary.php3">Glossary</a>
<a href="faq.php3">FAQ</a>

<a href="rss-news-reviews.php3" class="rss-icon">RSS feed</a></li>
<a target="_blank" href="https://www.facebook.com/GSMArenacom-189627474421/" class="fb-icon">Facebook</a>
<a target="_blank" href="http://twitter.com/gsmarena_com" class="tw-icon">Twitter</a>

</p>
<p>
&copy; 2000-2017 <a href="team.php3">GSMArena.com</a> 
<a href="http://www.gsmarena.com/switch.php3?ver=mobile&ref=MH5vb3N6QHZvd3BxekAoMicvKSsxb3dv">Mobile version</a>
<a href="contact.php3">Contact us</a>
<a href="advert.php3">Advertising</a>
<a href="privacy.php3">Privacy</a> 
<a href="terms.php3">Terms of use</a>
			
</p>			
<div id="cdn-hosting">
<a href="http://www.maxcdn.com/" target="_blank" rel="nofollow">
  <span class="center">CDN by</span><br />
  <img src="http://cdn2.gsmarena.com/w/css/maxcdn.gif" alt="" />
</a>
</div>
  </div>
 </div>
 
 

</div>


<script>
	(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	})(window,document,'script','//www.google-analytics.com/analytics.js','ga');

	ga('create', 'UA-131096-1', 'auto' );
	ga('send', 'pageview'
, { 'dimension2': '3' }
	);

</script>






</body></html>'''

soup = BeautifulSoup(input)
titleTag = soup.html.head.title.string
#print "Phone: " + titleTag
#print titleTag.string
#print len(soup('p'))
print ""
print ""
print "PART 1: PRINTING DATA FROM TABLE..."
print ""
print ""
print soup('li', {'class' : 'light pattern help help-popularity'})[0].strong
print ""
print "Technology: "
print soup('a', {'data-spec' : 'nettech'})[0].string
print ""
print "2G bands: "
print soup('td', {'data-spec' : 'net2g'})[0].string
print ""
print "3G bands: "
print soup('td', {'data-spec' : 'net3g'})[0].string
print ""
print "4G bands: "
print soup('td', {'data-spec' : 'net4g'})[0].string
print ""
print "Speed: "
print soup('td', {'data-spec' : 'speed'})[0].string
print ""
print "GPRS: "
print soup('td', {'data-spec' : 'gprstext'})[0].string
print ""
print "EDGE: "
print soup('td', {'data-spec' : 'edge'})[0].string
print ""
print "Announced: "
print soup('td', {'data-spec' : 'year'})[0].string
print ""
print "Status: "
print soup('td', {'data-spec' : 'status'})[0].string
print ""
print "Dimensions: "
print soup('td', {'data-spec' : 'dimensions'})[0].string
print ""
print "Weight: "
print soup('td', {'data-spec' : 'weight'})[0].string
print ""
print "SIM: "
print soup('td', {'data-spec' : 'sim'})[0].string
print ""
print "Other: "
print soup('td', {'data-spec' : 'bodyother'})[0]
print ""
print "Type: "
print soup('td', {'data-spec' : 'displaytype'})[0].string
print ""
print "Size:"
print soup.findAll(text="Size")[0].parent.parent.parent
print ""
print "displayresolution: "
print soup('td', {'data-spec' : 'displayresolution'})[0].string
print ""
print "Multitouch:"
print soup.findAll(text="Multitouch")[0].parent.parent.parent
print ""
print "Protection: "
print soup('td', {'data-spec' : 'displayprotection'})[0].string
print ""
print "displayother: "
print soup('td', {'data-spec' : 'displayother'})[0]
print ""
print "os: "
print soup('td', {'data-spec' : 'os'})[0].string
print ""
print "chipset: "
print soup('td', {'data-spec' : 'chipset'})[0].string
print ""
print "cpu: "
print soup('td', {'data-spec' : 'cpu'})[0].string
print ""
print "gpu: "
print soup('td', {'data-spec' : 'gpu'})[0].string
print ""
print "memoryslot: "
print soup('td', {'data-spec' : 'memoryslot'})[0].string
print ""
print "internalmemory: "
print soup('td', {'data-spec' : 'internalmemory'})[0].string
print ""
print "cameraprimary: "
print soup('td', {'data-spec' : 'cameraprimary'})[0]
print ""
print "camerafeatures: "
print soup('td', {'data-spec' : 'camerafeatures'})[0].string
print ""
print "cameravideo: "
print soup('td', {'data-spec' : 'cameravideo'})[0]
print ""
print "camerasecondary: "
print soup('td', {'data-spec' : 'camerasecondary'})[0].string
print ""
print "optionalother: "
print soup('td', {'data-spec' : 'optionalother'})[0]
print ""
print "wlan: "
print soup('td', {'data-spec' : 'wlan'})[0].string
print ""
print "bluetooth: "
print soup('td', {'data-spec' : 'bluetooth'})[0].string
print ""
print "gps: "
print soup('td', {'data-spec' : 'gps'})[0].string
print ""
print "nfc: "
print soup('td', {'data-spec' : 'nfc'})[0].string
print ""
print "radio: "
print soup('td', {'data-spec' : 'radio'})[0].string
print ""
print "usb: "
print soup('td', {'data-spec' : 'usb'})[0].string
print ""
print "sensors: "
print soup('td', {'data-spec' : 'sensors'})[0].string
print ""
print "featuresother: "
print soup('td', {'data-spec' : 'featuresother'})[0]
print ""
print "batdescription1: "
print soup('td', {'data-spec' : 'batdescription1'})[0].string
print ""
print "battalktime1: "
print soup('td', {'data-spec' : 'battalktime1'})[0].string
print ""
print "batmusicplayback1: "
print soup('td', {'data-spec' : 'batmusicplayback1'})[0].string
print ""
print "colors: "
print soup('td', {'data-spec' : 'colors'})[0].string
print ""
print "sar-us: "
print soup('td', {'data-spec' : 'sar-us'})[0].string
print ""
print "sar-eu: "
print soup('td', {'data-spec' : 'sar-eu'})[0].string
print ""
print "price: "
print soup('td', {'data-spec' : 'price'})[0].string
print ""
print "tbench: "
print soup('td', {'data-spec' : 'tbench'})[0]
print ""
print "batlife: "
print soup('td', {'data-spec' : 'batlife'})[0]
print ""
print ""
print "PART 2: PRINTING TABLE ROWS WITH CORRECT FORMATTING..."
print ""
print ""
def str2bool(v):
  return v.lower() in ("yes", "true", "t", "1", "available", "ja")
print "HSPA Speed in Mbps(int):"
print "Download:"
hspadl = float(soup('td', {'data-spec' : 'speed'})[0].string.split('Mbps')[0][5:9])
print hspadl
print "Upload:"
hspaul = float(soup('td', {'data-spec' : 'speed'})[0].string.split('Mbps')[0][10:14])
print hspaul
print "LTE Speed in Mbps(int):"
print "Download:"
ltedl = float(soup('td', {'data-spec' : 'speed'})[0].string.split(' ')[6][:3])
print ltedl
print "Upload:"
lteul = float(soup('td', {'data-spec' : 'speed'})[0].string.split(' ')[6][4:6])
print lteul
print "GPRS (bool):"
gprsbool = str2bool(soup('td', {'data-spec' : 'gprstext'})[0].string)
print gprsbool
print "EDGE (bool):"
edgebool = str2bool(soup('td', {'data-spec' : 'edge'})[0].string)
print edgebool
print "Announced: "
announcedint = int(float(soup('td', {'data-spec' : 'year'})[0].string.split(',')[0]))
print announcedint
print "Release: "
releaseint = int(float(soup('td', {'data-spec' : 'status'})[0].string.split(' ')[2][:4]))
print releaseint
print "Available: "
statusbool = str2bool(soup('td', {'data-spec' : 'status'})[0].string.split('.')[0])
print statusbool
print "Length in mm (int):"
length = float(soup('td', {'data-spec' : 'dimensions'})[0].string.split(' ')[0])
print length
print "Width in mm (int):"
width = float(soup('td', {'data-spec' : 'dimensions'})[0].string.split(' ')[2])
print width
print "Height in mm (int):"
height = float(soup('td', {'data-spec' : 'dimensions'})[0].string.split(' ')[4])
print height
print "Weight in grams (int):"
weight = int(float(soup('td', {'data-spec' : 'weight'})[0].string.split(' ')[0]))
print weight
print "Size in inches:"
displaysize = float(str(soup.findAll(text="Size")[0].parent.parent.parent).split('nfo')[1][2:5])
print displaysize
print ""
print ""
print "PART 3: PRINTING TABLE ROWS WITH BEAUTIFUL FORMATTING..."
print ""
print ""
print "Speed: " + "HSPA: " + str(hspadl) + "/" + str(hspaul) + " Mbps LTE : " + str(ltedl) + "/" + str(lteul) + " Mbps"
print "GPRS: " + str(gprsbool)
print "EDGE: " + str(edgebool)
print "Announced: " + str(announcedint)
print "Release: " + str(releaseint)
print "Available: "+ str(statusbool)
print "Dimensions: " + str(length) + " x " + str(width) + " x " + str(height) + " mm"
print "Weight: " + str(weight) + " g"
print "Size: " + str(displaysize) + " inches"

#for item in soup('tr'):
#    print item
#    print ""
#for item in soup('tr'):
#    if(item == "Yes"):
#      print str2bool(item)
#      print ""
#    elif(item == "No"):
#      print str2bool(item)
#      print ""
#    else:
#      print "None"
#gprstextbool = soup('td', {'data-spec' : 'gprstext'})[0].string
#print str2bool(gprstextbool)
#print "weight: "
#weight = int(float(soup('td', {'data-spec' : 'weight'})[0].string.split(' ')[0]))
#print weight
#weightn = weight.split(' ')[0]
#print int(float(weightn))
#bool result = False
#if(gprstextbool=="Yes"):
#    result = True
#else
#    result = False
#print result
#<strong class="accent"> <i class="head-icon icon-popularity"></i>28%</strong><span>20,862,149 hits</span></li><li class="light pattern help help-popularity">
#<strong class="accent"> <i class="head-icon icon-popularity"></i>28%</strong>
#span>20,862,149 hits</span></li>
#<li class="light pattern help help-fans">
#speed = soup('td', {'data-spec' : 'speed'})
#print speed.string
#print soup('p', {'id' : 'firstpara'}) [0] ['align']
#print soup.first('p').b.string
#print soup('p')[0].b.string
#print soup.nextSibling('p')
#td_tag = soup.find("td", class_="nfo")
#print td_tag
#a_tag = soup.find("a", href="network-bands.php3")
#print a_tag
#for tag in soup.findAll(re.compile("^b")):
#	print(tag.name)
#print soup.findAll("tbody")
#print tbody
#a = soup.body.div.div.div.div.div.table.tbody.tr.td.findAll("a")
#print a
#for item in soup.select('a.link-network-detail'):
#	print item
#print soup.findAll(text="Technology")
#print soup.findAll(text="Technology")[0].parent.parent.parent.parent.parent
#print soup.findAll(text="Technology")[0].parent.parent.parent
#for y in soup.findAll('td', attrs={'class': 'nfo'}):
#    print y.parent.contents
#tech = soup.find("td", {"class": re.compile("ttl")}).a.contents
#print tech
#for element in soup.find("td", {"class": re.compile("ttl")}).a:
#print element.text
