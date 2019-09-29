from bs4 import BeautifulSoup

response="""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:og="http://ogp.me/ns#">
<head id="ctl00_Head1"><title>
	A32 : Công ty cổ phần 32 | Tin tức và dữ liệu doanh nghiệp | CafeF.vn
</title><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /><meta id="ctl00_News_Keywords" name="news_keywords" content="A32, Công ty cổ phần 32, hồ sơ công ty, thông tin giao dịch , Tin tức và dữ liệu doanh nghiệp" /><meta id="ctl00_description" name="Description" content="Thông tin giao dịch và hồ sơ Công ty cổ phần 32 (mã: A32). Nhóm ngành: Da giầy, Chủ tịch HĐQT: Ông Vũ Xuân Tạo, Tổng Giám đốc: Ông Nguyễn Thế Anh, giá cổ phiếu: 27, P/E: 4.3" /><link rel="stylesheet" type="text/css" href="http://cafef3.vcmedia.vn/v2/style/solieu.v2.20161115.css" /><link href="http://cafef3.vcmedia.vn/mobile/m/styles/jquery-ui.css" rel="stylesheet" type="text/css" /><link href="http://cafef3.vcmedia.vn/v4/Style/stylev2.css" rel="stylesheet" /><link href="http://cafef3.vcmedia.vn/v4/Style/header.min.1.3.css" rel="stylesheet" /><link rel="stylesheet" type="text/css" href="http://cafef3.vcmedia.vn/v2/styles/stylesv3.20160226.css" />    
    <!--[if lte IE 6]><link rel="stylesheet" type="text/css" href="http://cafef3.vcmedia.vn/images/v3/ie618112013.css" /><![endif]-->
    <!--[if IE 7]><link rel="stylesheet" type="text/css" href="http://cafef3.vcmedia.vn/images/v3/ie718112013.css" /><![endif]-->
    <!--[if lte IE 7]><style type="text/css">#data-title-bar li span {display: none;}</style><![endif]-->
    <link href="http://cafef3.vcmedia.vn/v2/styles/tooltip.css" media="screen, projection" rel="stylesheet" type="text/css" /><link rel="shortcut icon" href="http://cafef3.vcmedia.vn/v2/images/favicon.ico" />
    <script type="text/javascript">var servertime = parseFloat('175805'); var _symbol = 'A32'; var domain = ""; var rewrite = true;</script>
    <script src='http://cafef3.vcmedia.vn/v2/kby/fc216c5f-ba6e-4587-9fb8-9ea14e20a85b/kby.js' type="text/javascript"></script>
    <script src="http://cafef3.vcmedia.vn/js/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script type="text/javascript" src="http://cafef3.vcmedia.vn/v2/scripts/initSearchBox.js"></script>
       <script type="text/javascript" src="http://cafef3.vcmedia.vn/v4/scripts/stock.min.1.4.js"></script>
    <script type="text/javascript" src="http://mingid.vcmedia.vn/js/mingid_core.js"></script>
    <script src="http://cafef3.vcmedia.vn/v2/scripts/cafef.20170116.js" type="text/javascript"></script>
    <script type="text/javascript" src="http://cafef3.vcmedia.vn/v2/scripts/jquery.tools.min.js"></script>
    <script type="text/javascript" src="http://cafef3.vcmedia.vn/v2/scripts/jquery-ui.js"></script>
    <script type="text/javascript" src="http://cafef3.vcmedia.vn/v2/scripts/compatibilityv3.js"></script>
    <script type="text/javascript" src="http://cafef3.vcmedia.vn/v2/scripts/inlinestockpage.20120816.js"></script>
    <script type="text/javascript" src="http://cafef3.vcmedia.vn/v2/scripts/slimScroll.js"></script>
    <!--[if lte IE 6]><script type="text/javascript" src="http://cafef3.vcmedia.vn/v2/ie/iepngfix_tilebg.js"></script><![endif]-->
    <!-- Begin comScore Tag -->
    <script>
        var _comscore = _comscore || [];
        _comscore.push({ c1: "2", c2: "17793284" });
        (function () {
            var s = document.createElement("script"), el = document.getElementsByTagName("script")[0]; s.async = true;
            s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";
            el.parentNode.insertBefore(s, el);
        })();
    </script>
    <!-- End comScore Tag -->
    <script>
        (function (i, s, o, g, r, a, m) {
            i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
                (i[r].q = i[r].q || []).push(arguments)
            }, i[r].l = 1 * new Date(); a = s.createElement(o),
            m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
        })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

        ga('create', 'UA-34575478-39', 'auto');
        ga('send', 'pageview');

        ga('create', 'UA-34575478-17', 'auto', { 'name': 'pagecafef' });
        ga('pagecafef.send', 'pageview');
    </script>
    <script type='text/javascript' src="//media1.admicro.vn/core/adm_tracking.js"></script>
<meta property="fb:app_id" content="115279665149396" /><meta property="og:title" content="A32 : Công ty cổ phần 32 | Tin tức và dữ liệu doanh nghiệp | CafeF.vn" /><meta property="og:type" content="company" /><meta property="og:site_name" content="CafeF.vn" /><meta property="og:url" content="http://s.cafef.vn/upcom/A32-cong-ty-co-phan-32.chn" /><meta property="og:image" content="http://cafef.vcmedia.vn/A32.JPG" /><meta property="og:description" content="Thông tin giao dịch và hồ sơ Công ty cổ phần 32 (mã: A32). Nhóm ngành: Da giầy, Chủ tịch HĐQT: Ông Vũ Xuân Tạo, Tổng Giám đốc: Ông Nguyễn Thế Anh, giá cổ phiếu: 27, P/E: 4.3" /><link rel="canonical" href="http://s.cafef.vn/upcom/A32-cong-ty-co-phan-32.chn" /><link rel="alternate" href="http://m.cafef.vn/upcom/A32-cong-ty-co-phan-32.chn" media="handheld" /><link rel="image_src" href="http://cafef.vcmedia.vn/A32.JPG" /></head>
<body style="background-color: #fff;">
    <script type="text/javascript">
        /*(function() {
            var em = document.createElement('script'); em.type = 'text/javascript'; em.async = true;
            em.src = ('https:' == document.location.protocol ? 'https://vn-ssl' : 'http://vn-cdn') + '.effectivemeasure.net/em.js';
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(em, s);
        })();*/
    </script>
    

    <form name="aspnetForm" method="post" action="/upcom/A32-cong-ty-co-phan-32.chn" id="aspnetForm">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTE3NDQ2NzQ1NTNkZElRvEK5cbARarethfVvga8w50Sz" />

<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="D891974B" />
        <div>
            
    
    
<div class="header clearfix">
    <div class="header_logo">
        <div class="wp1040 relative">
            <div class="logo">
                <a href="/" class="sprite" title="Kênh thông tin kinh tế - tài chính Việt Nam"></a>
            </div>
            
            <a href="http://comment.v1.vietid.net/comments?app_key=09e776cfdcf813daf939719ded62d915&content_url=http://cafef.vn/news-20151222155837958.chn&news_title=TSVlMSViYiU5ZGkrYiVlMSViYSVhMW4rJWM0JTkxJWUxJWJiJThkYyt0ciVlMSViYSVhM2krbmdoaSVlMSViYiU4N20rdiVjMyVhMCtnJWMzJWIzcCslYzMlYmQrdiVlMSViYiU4MStnaWFvK2RpJWUxJWJiJTg3bittJWUxJWJiJTliaStjaG8rdHJhbmcrdGluK3QlYzMlYTBpK2NoJWMzJWFkbmgrQ2FmZUY=&num_count=5&debugcache=1&min=0&scroll=0&http_referer=http://cafef.vn/thoi-su/moi-ban-doc-trai-nghiem-va-gop-y-ve-giao-dien-moi-cho-trang-tin-tai-chinh-cafef-20151222155837958.chn&verify=1&verify_flag=53a1b739f4a5d3c8bd94f458d21f8380&funny_flag=0&height=238&iframe_comment_id=mingid_comment_iframe&comment_flag=0&news_url_short=0&real_time=undefined&is_hidden_comment=0" target="_blank" rel="nofollow"
                class="fancybox fancybox.iframe fl"
                id="OpenGopYF" style="margin-left: 74px;">
                <i class="moibandocgopy sprite"></i>
            </a>
            <div class="time" id="datetime" style="display: none;">&nbsp;</div>
            
<div class="mack" id="CafeF_StockSymbolContainer">
    <div id="macktheodoi" class="inner" data-type="stock-container"></div>
</div>
        </div>
    </div>
    <div class="header_new clearfix">
        <div class="wp1040">
            <div class="menupage">
                <a class="sprite top isent" href="http://cafef.vn/gui-tin-nhanh.chn" title="Gửi tin nhanh"><span class="icon_sent"></span>Gửi tin nhanh</a>
                <a class="idautu" href="http://liveboard.cafef.vn" target="_blank" rel="nofollow" title="Bản giá điện tử"><span class="icon_sent sprite"></span>Bảng giá điện tử</a>
                <a class="sprite end itable" target="_blank" rel="nofollow" href="http://s.cafef.vn/danh-muc-dau-tu.chn" title="Danh mục đầu tư"><span class="icon_sent"></span>Danh mục đầu tư</a>
                <div id="liuseraccount" style="display: none;">
                    <ul style="width: 165px;" id="ulAccount">
                        <li>
                            <a style="font-weight: normal;" onclick="vietidlogout()" href="javascript:void()" title="Thoát khỏi danh mục">Thoát</a></li>
                        <li>
                            <a style="font-weight: normal;" href="/thay-doi-mat-khau.chn" title="Đổi mật khẩu">Đổi mật khẩu</a></li>
                    </ul>
                    <div id="useraccount"></div>
                </div>
            </div>
            
<div class="tinmoi">
    <div class="title_box">
        <p class="title_left">TIN MỚI!</p>
        <a href="/doc-nhanh.chn" title="đọc nhanh" class="doctinnhanh">Đọc nhanh >></a>
    </div>
    <div class="clearfix"></div>
    <div class="list_news">
        <div id="listNewHeader" dmtb="4">
            <ul>

            </ul>

        </div>
    </div>
</div>


            
<div class="bieudo_header">
    <div class="bieudo1">
        <p class="index_ck">
            VN-Index:
            <b class="idx_1"></b><span class="idc_1"></span><span class="idp_1"></span>
        </p>
        <p class="gia_ck">GTGD: <span class="idv_1"></span>tỷ VNĐ</p>
        <div id="headerchart1" class="img_bieudo"></div>
    </div>
    <div class="bieudo2">
        <p class="index_ck">
            HNX-Index:
            <b class="idx_2"></b><span class="idc_2"></span><span class="idp_2"></span>
        </p>
        <p class="gia_ck">GTGD: <span class="idv_2"></span>tỷ VNĐ</p>
        <div id="headerchart2" class="img_bieudo"></div>
    </div>
</div>

<script type="text/javascript">
    var currentTime = parseFloat('175805');
</script>




<script type="text/javascript">


    function LoadUser2() { convertCookie(); var userName = getCookie('cafef.user.v2', 'name'); if (userName == undefined) { userName = ''; }; if (userName.indexOf('&name=') > 0) { userName = userName.substr(userName.indexOf('&name=') + 6, 50); if (userName.indexOf('&') > 0) { userName = userName.substr(0, userName.indexOf('&')); } } if (userName.indexOf('&') >= 0) { userName = ''; } if (userName != null && userName != '' && userName != 'undefined') { $("#liuseraccount").show(); $("#useraccount").html('<a href="http://cafef.vn/danh-muc-dau-tu.chn" style="color:red; font-weight:bold">&nbsp;' + userName + '&nbsp;</a>'); $.ajax({ url: "/ajax/user.aspx", success: function (data) { if (data == '' || data == '0') { minglogin(true); } } }); closeMingNote(false); } else { displayMingNote(); $('#danhmucdautu').click(function (e) { e.preventDefault(); minglogin(false); }); } }
    
    var isTrading = true;

    LoadUser2();
   

    var lastTimeHead = '2019/09/29 17:58:05';
    function vietidlogout() {
        openMyModal('http://v1.vietid.net/OauthServerV2/logout?app_key=09e776cfdcf813daf939719ded62d915&call_back=http://s.cafef.vn/pages/signout.aspx', 510, 470, false);
        return false;
    }
    $(function () {
        $("#liuseraccount").mouseover(function () {
            $("#ulAccount").css("display", "block");
        });
        $("#liuseraccount").mouseout(function () {
            $("#ulAccount").css("display", "none");
        });
    });
</script>

        </div>
    </div>
    <div class="clearfix"></div>
    <div class="menucategory menuheader clearfix" id="menu_wrap">
        <div class="wp1040 relative">
            <ul>
                <li class="bt_home active"><a href="//cafef.vn" title="Trang chủ" class="sprite"></a></li>
                <li class="li_left"><a href="//cafef.vn/thoi-su.chn" title="THỜI SỰ">THỜI SỰ</a></li>
                <li><a href="//cafef.vn/thi-truong-chung-khoan.chn" title="CHỨNG KHOÁN">CHỨNG KHOÁN</a></li>
                <li><a href="//cafef.vn/bat-dong-san.chn" title="BẤT ĐỘNG SẢN">BẤT ĐỘNG SẢN</a></li>
                <li><a href="//cafef.vn/doanh-nghiep.chn" title="DOANH NGHIỆP">DOANH NGHIỆP</a></li>
                <li><a href="//cafef.vn/tai-chinh-ngan-hang.chn" title="NGÂN HÀNG">NGÂN HÀNG</a></li>
                <li><a href="//cafef.vn/tai-chinh-quoc-te.chn" title="TÀI CHÍNH QUỐC TẾ">TÀI CHÍNH QUỐC TẾ</a></li>
                <li><a href="//cafef.vn/vi-mo-dau-tu.chn" title="VĨ MÔ">VĨ MÔ</a></li>
                <li><a href="//cafef.vn/song.chn" title="SỐNG">SỐNG</a></li>
                <li><a href="//cafef.vn/hang-hoa-nguyen-lieu.chn" title="HÀNG HÓA">HÀNG HÓA</a></li>
                
                <li class="menucategory_right"><a href="http://s.cafef.vn/top/ceo.chn" title="Top 200">Top 200</a></li>
                <li class="menucategory_right"><a href="http://s.cafef.vn/du-lieu.chn" title="Dữ liệu">Dữ liệu</a></li>

            </ul>
        </div>
    </div>
</div>

    <div id="pagewrap">
        <div id="container" class="clearfix">
            
         
            <div style="overflow: hidden; padding-bottom: 10px">
                <script type="text/javascript" src="http://admicro1.vcmedia.vn/ads_codes/ads_box_96.ads"></script>
            </div>
            
            <div class="botop">
                <div style="padding-top: 10px;">
                    
                </div>
                <div class="contentMain">
                    <div id="content">
                        <div class="dulieu">
                            <h2 class="cattitle">Thông tin giao dịch</h2>
                            <!-- // CacChiSo -->
                            
<style type="text/css">
    .dl-title {
        padding: 8px 0 0px 12px;
    }

    #symbolbox {
        float: left;
        border: 1px solid #EEE;
        padding: 5px 15px 5px 15px;
        border-bottom: none;
    }

    .kyquy {
        padding-left: 35px;
        color: #666;
        padding-bottom: 5px;
        padding-top: 5px;
    }

    .kyquyservice {
        padding-left: 35px;
        color: #666;
    }

    #namebox {
        float: left;
        padding-top: 5px;
        padding-left: 15px;
    }

        #namebox h1 {
            font-size: 16px;
        }

    .logo_intro {
    }

    .avartar {float:left;
    }

    .companyIntro {
        font-weight: normal;
        font-family: Arial;
        font-size: 13px;
        margin-top: 15px; margin-right:5px;
    }
</style>

<div style="float: left; display: none;" class="breadcrumb">
    <div itemtype="http://data-vocabulary.org/Breadcrumb" itemscope="">
        <a itemprop="url" href="http://cafef.vn"><span itemprop="title">CafeF.vn</span></a> &gt;
    </div>
    <div itemtype='http://data-vocabulary.org/Breadcrumb' itemscope=''>
        <a href='http://s.cafef.vn/du-lieu.chn' title='Dữ liệu' itemprop='url'><span itemprop='title'>Dữ liệu</span></a>
    </div>
</div>
<div class="dl-title clearfix">
    <div id="symbolbox">
        A32
    </div>
    <div id="namebox" class="dlt-ten">
        <h1>&nbsp;Công ty cổ phần 32 (UpCOM)
    </div>
</div>

<div class="kyquy">
    </div>

<div class="kyquyservice">
    </div>

<div class="logo_intro clearfix">
    
    <div class="avartar">
        <img style="width: 100px; margin: 5px 10px;" alt="Công ty cổ phần 32" src="http://images1.cafef.vn/Images/Uploaded/DuLieuDownload/logodn/A32.JPG" /></div>
    
    <div class="companyIntro">Công ty Cổ phần 32 – một trong những doanh nghiệp hàng đầu trong ngành Giày – May tại Việt Nam. Chúng tôi luôn tự hào vì được đối tác khách hàng, người tiêu dùng tin tưởng và lựa chọn, là nguồn động viên, cổ vũ lớn lao để doanh nghiệp“ Vững bước trên mọi nẻo đường”.</div>
    
</div>

                            
                            
                            
<script type="text/javascript">
    var IE = document.all ? true : false;
    var folder = '20190928';
    var nB;
    if (!IE) document.captureEvents(Event.MOUSEMOVE);
    document.onmousemove = getMouseXY;
    var tempX = 0;
    var tempY = 0;
    function getMouseXY(e) {
        if (IE) {
            tempX = event.clientX + document.body.scrollLeft;
            tempY = event.clientY + document.body.scrollTop;
        } else {
            tempX = e.pageX;
            tempY = e.pageY;
        }
        if (tempX < 0) { tempX = 0; }
        if (tempY < 0) { tempY = 0; }
        return true;
    }
    function ShowDetailBox() {
        var divCompanyInfo = document.getElementById('divCompanyInfo');
        divCompanyInfo.style.display = 'block';
        divCompanyInfo.style.left = tempX;
    }
    function HideDetailBox() {
        var divCompanyInfo = document.getElementById('divCompanyInfo');
        divCompanyInfo.style.display = 'none';
    }
    function SetFirst() {
        var sym = 'A32';
     var bTrade = 'False';
     if (bTrade == 'True') {
         ChangeImage('1day', 'lnkChart_1day');
     }
     else {
         ChangeImage('6months', 'lnkChart_6months');
         //var url = "http://cafef4.vcmedia.vn/" + folder + "/" + sym + "/6months.png";
         //document.getElementById('imgChart').setAttribute('src',url);    
     }
 }
</script>

<style type="text/css">
    #lkKhopLenh img {
        width: 260px;
    }

    .dothi img {
        width: 260px;
    }
</style>

<style>
    .eq {
        color: #FF9900 !important;
    }

    .down {
        color: #CC0000 !important;
    }
    .pink{color:#FF00FF !important;}
    .up {
        color: #00A500 !important;
    }

    .fl {
        color: #006699 !important;
    }

    .ce {
    color:#FF00FF !important;
    }

    .v1 {
        float: left;
        margin-right: 10px;
        color: #003366;
        font-weight: bold;
        margin-top: 3px;
    }

    .v2 {
        float: left;
    color: #222;
    font-size: 16px;
    text-align: right;
    font-weight: bold;
    width: 85px;
    }
    .right {
        text-align:right;
    }
</style>
<div class="dl-thongtin clearfix" style="padding-bottom: 0;">
    <div class="dlt-left">
        
        <div class="dltl-update">
            
            <div class="dltlu-time">
                Cập nhật lúc 14:15 Thứ 6, 27/09/2019
            </div>
            
                <div class='dltlu-point up'>27</div>
            
            <span id="CC">
                <div class='dltlu-up green'>&nbsp; 3.4 (14.4%)</div></span>
            <div class="clearfix" style="margin:7px 0px;">
                <div class="v1">Khối lượng</div>
                <div class="v2" id="CV">
                    1,100
                </div>
            </div>
            <div class="dltlu-time" style="padding-top: 5px; padding-left: 13px;">Đóng cửa</div>
        </div>
        <div class="dltl-price">
            <ul>
                <li class="clearfix">
                    <div class="l">Giá tham chiếu</div>
                    <div class="eq r" id="REF">
                        23.6
                    </div>
                </li>
                   <li class="clearfix">
                    <div class="l">Giá trần</div>
                    <div class="r pink" id="CE">
                        27.1
                    </div>
                </li>
                   <li class="clearfix">
                    <div class="l">Giá sàn</div>
                    <div class="r fl" id="FL">
                        20.1
                    </div>
                </li>
                <li class="clearfix">
                    <div class="l">Giá mở cửa</div>
                        <div class='right up'>27</div>
                </li>
                <li class="clearfix">
                    <div class="l">Giá cao nhất</div>
                        <div class='right up'>27</div>
                </li>
                <li class="clearfix">
                    <div class="l">Giá thấp nhất</div>
                        <div class='right up'>27</div>
                </li>
              
                <li class="clearfix" style="margin-top: 10px;border-top: 1px solid #eee;padding: 0px;margin-bottom: 0px;height: 5px;">&nbsp;</li>
                <li class="clearfix">
                    <div class="l">
                        GD ròng NĐTNN
                    </div>
                    <div class="right">
                        0
                    </div>
                </li>
                
                <li id="ctl00_ContentPlaceHolder1_ucTradeInfo_divRoomNNConlai" class="clearfix">
                    <div class="l">Room NN còn lại</div>
                    <div class="right" >
                        49.00
                        (%)
                    </div>
                </li>
            </ul>
            <div class="dltlnote">Đơn vị giá: 1000 VNĐ</div>
        </div>
        
        <div class="dltl-other" style="">
            
            <ul>
                
                <div id="ctl00_ContentPlaceHolder1_ucTradeInfo_pnEPS">
	
                    <li class="clearfix">
                        <div class="l"><b>(*)&nbsp;&nbsp; <a href="/upcom/A32/chi-tiet-tinh-EPS.chn">EPS cơ bản</a></b> (nghìn đồng):</div>
                        <div class="r">
                            6.34
                        </div>
                    </li>
                    <li id="ctl00_ContentPlaceHolder1_ucTradeInfo_liEPSDieuChinh" class="clearfix">
                        <div class="l"><b>&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; <a href="/upcom/A32/chi-tiet-tinh-EPS.chn">EPS pha loãng</a></b> (nghìn đồng):</div>
                        <div class="r">
                            6.34
                        </div>
                    </li>
                    <li class="clearfix">
                        <div class="l"><b>&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; P/E :</b></div>
                        <div class="r">
                            4.26
                        </div>
                    </li>
                
</div>
                <li class="clearfix">
                    <div class="l"><b>&nbsp; &nbsp;&nbsp;&nbsp;&nbsp; Giá trị sổ sách /cp</b> (nghìn đồng):</div>
                    <div class="r">
                        29.53
                    </div>
                </li>
                <li class="clearfix">
                    <div class="l"><b>(**) Hệ số beta:</b></div>
                    <div class="r">
                        n/a
                    </div>
                </li>
                <li class="clearfix">
                    <div class="l"><b>KLGD khớp lệnh trung bình 10 phiên:</b></div>
                    <div class="r">
                        790
                    </div>
                </li>

                <li class="clearfix">
                    <div class="l"><b>KLCP đang niêm yết:</b></div>
                    <div class="r">
                        6,800,000
                    </div>
                </li>

                <li class="clearfix">
                    <div class="l"><b>KLCP đang lưu hành:</b></div>
                    <div class="r">
                        6,800,000
                    </div>
                </li>
                <li class="clearfix">
                    <div class="l"><b>Vốn hóa thị trường</b> (tỷ đồng):</div>
                    <div class="r">
                        183.60
                    </div>
                </li>
            </ul>
            <div class="dltlonote">
                <div id="ctl00_ContentPlaceHolder1_ucTradeInfo_pnEPSNote" style="display: inline;">
	
                    (*)
                    Số liệu EPS tính tới năm 2018
                    | <a href="/upcom/A32/chi-tiet-tinh-EPS.chn">Xem cách tính</a><br />
                
</div>
                (**) Hệ số beta tính với dữ liệu 100 phiên | <a href="/help/hesobeta.aspx">Xem cách tính</a>
            </div>
        </div>
    </div>
    <!-- // left -->
    <div class="dlt-right">
        
        <div class="dothi">
            <p>
                <a href="/Thi-truong-niem-yet/Bieu-do-ky-thuat/EPS-A32-2.chn" target="_blank"><b>Xem đồ thị kỹ thuật
            
                </b></a>
            </p>
            <a href="/Lich-su-giao-dich-A32-1.chn" id="lkChart">
                <img src="" alt="" border="0" width="260" id="imgChart" /></a>
            <a href="/Lich-su-giao-dich-A32-6.chn" id="lkKhopLenh" style="display: none;" rel="start"></a>
        </div>
        <div class="dothi-note clearfix" id="divChart">
            <div class="dltr-l">Đồ thị vẽ theo giá điều chỉnh</div>
            <div class="dltr-r">đv KLg: 10,000cp</div>
        </div>
        <div class="dothi-note clearfix" id="divKhopLenh" style="display: none">
            <div class="dltr-l"><a href='/Lich-su-giao-dich-A32-6.chn'>Xem khớp lệnh theo từng lô</a></div>
            <div class="dltr-r">đv KLg: 1 cp</div>
        </div>
        <div class="dltr-time">
            <a style="padding-left: 4px;" id="lnkChart_1day" href="javascript:void(0)" onclick="ChangeImage('1day', 'lnkChart_1day');">1 ngày</a> | 
            <a id="lnkChart_7days" href="javascript:void(0)" onclick="ChangeImage('7days', 'lnkChart_7days');">1 tuần</a> | <a id="lnkChart_1month" href="javascript:void(0)" onclick="ChangeImage('1month', 'lnkChart_1month');">1 tháng</a> | <a id="lnkChart_3months" href="javascript:void(0)" onclick="ChangeImage('3months', 'lnkChart_3months');">3 tháng</a> | <a style="color: #CC0001;" id="lnkChart_6months" href="javascript:void(0)"
                onclick="ChangeImage('6months', 'lnkChart_6months');">6 tháng</a>
            <br />
            <a id="lnkChart_1year" href="javascript:void(0)" onclick="ChangeImage('1year', 'lnkChart_1year');">1 năm</a> | 
                 <a id="lnkChart_3year" href="javascript:void(0)" onclick="ChangeImage('3years', 'lnkChart_3year');">3 năm</a>
            | <a id="lnkChart_all" href="javascript:void(0)" onclick="ChangeImage('all', 'lnkChart_all');">tất cả</a>
            <br />

        </div>
        
        <div class="dltr-other">
            

            <div>
                Ngày giao dịch đầu tiên: <b>
                    23/10/2018</b>
            </div>
            <div>
                Giá đóng cửa phiên GD đầu tiên(nghìn đồng): <b>
                    25.9</b>
            </div>
            <div>
                Khối lượng cổ phiếu niêm yết lần đầu: <b>
                    6,800,000</b>
            </div>
            <div class="tt" style="font-size: 11px; color: #000072; font-weight: bold; font-family: tahoma, verdana, arial;">
                <a style="font-size: 11px; cursor: pointer;" class="dangky">Lịch sử trả cổ tức và chia thưởng</a><div class="tooltip">
                    <div class="top"></div>
                    <div class="middle" style="padding-left: 10px; font-weight: normal">
                        - <b>06/06/2019</b>: Cổ tức bằng Tiền, tỷ lệ 7%<br />- <b>08/01/2019</b>: Cổ tức bằng Tiền, tỷ lệ 15%<br />
                    </div>
                    <div class="bottom">
                        (*) Ngày hiển thị là ngày GD không hưởng quyền<br />
                        <font style='color: #004370'>(**) Ngày hiển thị là ngày phát hành</font>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
<script type="text/javascript">
    function ChangeImage(id, lnk) {
        if ($('#divChart').length == 0) return;
        if (id == '1day') {
            if ($("#lkKhopLenh").attr("rel") == "start") {
                $("#lkKhopLenh").html("<img src='/chartindex/pricechart.ashx?symbol=A32&type=price&date=27/09/2019&width=380&height=250&rd=000000' alt='' border='0' onerror='ChangeImage(\"6months\", \"lnkChart_6months\");' /><img src='/chartindex/pricechart.ashx?symbol=A32&type=volume&date=27/09/2019&rd=000000' alt='' border='0' onerror='ChangeImage(\"6months\", \"lnkChart_6months\");' />");
            }
            $('#lkKhopLenh').show();
            $('#lkChart').hide();
            $('#divKhopLenh').show();
            $('#divChart').hide();
        } else {
            $('#lkKhopLenh').hide();
            $('#lkChart').show();
            $('#divKhopLenh').hide();
            $('#divChart').show();
            document.getElementById('imgChart').setAttribute('src', 'http://cafef4.vcmedia.vn/' + folder + '/' + 'A32' + '/' + id + '.png');
    }
    document.getElementById('lnkChart_7days').style.color = '#013567';
    document.getElementById('lnkChart_1month').style.color = '#013567';
    document.getElementById('lnkChart_3months').style.color = '#013567';
    document.getElementById('lnkChart_6months').style.color = '#013567';
    document.getElementById('lnkChart_1year').style.color = '#013567';
    document.getElementById('lnkChart_1day').style.color = '#013567';
    document.getElementById('lnkChart_3year').style.color = '#013567';
    document.getElementById('lnkChart_all').style.color = '#013567';
    document.getElementById(lnk).style.color = '#CC0001';
}
SetFirst();

</script>


                            

                            <!-- // End -->
                            <div class="tracuu clearfix">
                                <a href="/Lich-su-giao-dich-A32-1.chn" class="tc-ls">Tra cứu dữ liệu lịch sử</a> <a href="/Lich-su-giao-dich-A32-4.chn" class="tc-cd" style="border-right: 1px solid #EEE;">Tra cứu GD cổ đông lớn &amp; cổ đông nội bộ</a>
                               
                                <img style="float: left; padding-left: 5px; margin-top: 3px;" alt="" src="http://cafef3.vcmedia.vn/v2/images/report_bug_btn_red.png" /><a style="float: left; padding: 3px 0px 3px 5px; background: none;" href="javascript:void(0)" onclick="popupsend()">Báo lỗi dữ liệu</a>
                            </div>
                            <!-- //Tin tức - Sự kiện -->
                            
<div class="tintucsukien" style="padding-top:10px">
    <div style="float:right;"><a href="/tin-doanh-nghiep/a32/Event.chn" id="aViewMoreLink">Xem tất cả</a></div>
    <h2 class="cattitle noborder">Tin tức - Sự kiện</h2>
    <div id="divTopEvents">
        
                <ul>
            
                <li style="line-height:20px"><a href="/a32-322443/a32-ong-nguyen-the-anh-pho-chu-tich-hdqt-dang-ky-mua-20000-cp.chn" title="A32: &#212;ng Nguyễn Thế Anh - Ph&#243; Chủ tịch HĐQT đăng k&#253; mua 20.000 CP">A32: Ông Nguyễn Thế Anh - Phó Chủ tịch HĐQT đăng ký mua 20.000 CP</a> (13/09/2019 08:28)</li>
            
                <li style="line-height:20px"><a href="/a32-314278/a32-ong-nguyen-the-anh-pho-chu-tich-hdqt-da-mua-2800-cp.chn" title="A32: &#212;ng Nguyễn Thế Anh - Ph&#243; Chủ tịch HĐQT đ&#227; mua 2.800 CP">A32: Ông Nguyễn Thế Anh - Phó Chủ tịch HĐQT đã mua 2.800 CP</a> (10/07/2019 09:34)</li>
            
                <li style="line-height:20px"><a href="/a32-312903/a32-ong-nguyen-the-anh-pho-chu-tich-hdqt-dang-ky-mua-2800-cp.chn" title="A32: &#212;ng Nguyễn Thế Anh - Ph&#243; Chủ tịch HĐQT đăng k&#253; mua 2.800 CP">A32: Ông Nguyễn Thế Anh - Phó Chủ tịch HĐQT đăng ký mua 2.800 CP</a> (01/07/2019 14:21)</li>
            
                <li style="line-height:20px"><a href="/a32-309371/diem-danh-nhung-doanh-nghiep-chot-quyen-nhan-co-tuc-bang-tien-bang-co-phieu-va-co-phieu-thuong-tuan-nay.chn" title="Điểm danh những doanh nghiệp chốt quyền nhận cổ tức bằng tiền, bằng cổ phiếu v&#224; cổ phiếu thưởng tuần n&#224;y">Điểm danh những doanh nghiệp chốt quyền nhận cổ tức bằng tiền, bằng cổ phiếu và cổ phiếu thưởng tuần này</a> (03/06/2019 08:55)</li>
            
                <li style="line-height:20px"><a href="/a32-308683/lich-chot-quyen-nhan-co-tuc-bang-tien-cua-8-doanh-nghiep.chn" title="Lịch chốt quyền nhận cổ tức bằng tiền của 8 doanh nghiệp">Lịch chốt quyền nhận cổ tức bằng tiền của 8 doanh nghiệp</a> (28/05/2019 13:46)</li>
            
                <li style="line-height:20px"><a href="/a32-308769/a32-662019-ngay-gdkhq-tra-co-tuc-bang-tien-mat-700dcp.chn" title="A32: 6.6.2019, ng&#224;y GDKHQ trả cổ tức bằng tiền mặt (700đ/cp)">A32: 6.6.2019, ngày GDKHQ trả cổ tức bằng tiền mặt (700đ/cp)</a> (28/05/2019 13:27)</li>
            
                </ul>
                    
    </div>
    <div class="xemtiep2 clearfix">
  	        
            <div class="paging">
               <span id="spanPre"  style="font-weight:bold; font-family:Tahoma; font-size:9px; color:#B2B2B2">&lt;&lt; Trước</span>&nbsp;&nbsp;&nbsp;&nbsp;
               <span id="spanNext"><a id="aNext" style="font-weight:bold; font-family:Tahoma; font-size:9px; color:#C00" href="javascript:LoadNext();">Sau &gt;&gt;</a></span>
            </div>
        </div>
    <div class="loctin">
        <strong>Lọc tin</strong>:  
        <a href="javascript:void(0);" name="aLink" id="a0" onclick="LoadEventsRelatedNews('a32',0,1,6);">Tất cả</a> 
        | <a href="javascript:void(0);" name="aLink" id="a2" onclick="LoadEventsRelatedNews('a32',2,1,6);">Trả cổ tức - Chốt quyền</a> 
        | <a href="javascript:void(0);" name="aLink" id="a1" onclick="LoadEventsRelatedNews('a32',1,1,6);">Tình hình SXKD & Phân tích khác</a>  
        | <a name="aLink" id="a4" href="javascript:void(0);" onclick="LoadEventsRelatedNews('a32',4,1,6);">Tăng vốn - Cổ phiếu quỹ</a>  
        | <br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <a name="aLink" id="a5" href="javascript:void(0);" onclick="LoadEventsRelatedNews('a32',5,1,6);"> GD cổ đông lớn & Cổ đông nội bộ</a>  
        | <a name="aLink" id="a3" href="javascript:void(0);" onclick="LoadEventsRelatedNews('a32',3,1,6);">Thay đổi nhân sự</a>
    </div>
</div>
<input id="hdConfigID" type="hidden" value="0" />
<input id="hdPageIndex" type="hidden" value="1" />
<input id="hdSymbol" type="hidden" value="a32" />

<script type="text/javascript">
var _symbol = 'a32';
var hdconfigid = document.getElementById('hdConfigID');
var hdpageindex = document.getElementById('hdPageIndex');
var hdsymbol = document.getElementById('hdSymbol');
var anext = document.getElementById('aNext');
var apre = document.getElementById('aPre');     
var spannext = document.getElementById('spanNext');
var spanpre = document.getElementById('spanPre');  
var countTotal; 
function LoadNext()
{
    var index = hdpageindex.value;       
    var configid =  hdconfigid.value;    
    var symbol =     hdsymbol.value;   
    index = eval(eval(index) + 1);      
    LoadEventsRelatedNews(symbol,configid, index,6);
}
function LoadPre()
{
    var index = hdpageindex.value;       
    var configid =  hdconfigid.value;    
    var symbol =     hdsymbol.value;   
    if(index >"1")
    {
        index = eval(eval(index) - 1);
        LoadEventsRelatedNews(symbol,configid, index,6);    
    }        
}
function LoadEventsRelatedNews(symbol, configID, index, size)
{  
    $.ajax({
		type: "GET",
		url: "/Ajax/NewsBySymbol.aspx",
		data: "symbol="+ _symbol + "&configID=" + configID + "&PageIndex=" + index + "&PageSize=" + size + "&Type=1",
		success: function(msg){
		     document.getElementById("divTopEvents").innerHTML=msg;
		     if (msg=="")
		        hdpageindex.value ="1";
		}
	});
//	$.ajax({
//		type: "GET",
//		url: "/Ajax/GetTotalPage.aspx",
//		data: "symbol="+ _symbol + "&configID=" + configID + "&PageIndex=" + index + "&PageSize=" + size + "&Type=1",
//		success: function(msg){
//		     GetTotalCount(msg, index);
//		}
//	});
	GetTotalCount(index);
	GetALink(configID);
    hdpageindex.value = index;
    hdconfigid.value = configID;
    hdsymbol.value = symbol;
    var alink = document.getElementById('aViewMoreLink');
    if(configID!="0")
    {
        alink.href ='/Tin-doanh-nghiep/'+ symbol +'/'+ configID +'/Event.chn'
    }
    else
    {
        alink.href ='/Tin-doanh-nghiep/'+ symbol +'/Event.chn'
    }
} 
function GetALink(id)
{
    var aID = document.getElementById('a' + id);
    var aLink = document.getElementsByName('aLink');
    
    for(i=0; i< aLink.length; i++)
    {
        aLink[i].style.color="";
    }
    aID.style.color = "#CC0001";
}
function GetTotalCount( ide)
{        
//    countTotal = total;
//    if(ide>=countTotal)
//    {
//        spannext.innerHTML = "<span style=\"font-weight:bold; font-family:Tahoma; font-size:9px; color:#B2B2B2\">Sau >></span>";
//    }
//    else
//    {
//        spannext.innerHTML = "<a style=\"font-weight:bold; font-family:Tahoma; font-size:9px; color:#C00\" id=\"aNext\" href=\"javascript:LoadNext();\">Sau >></a>";
//    }
    if(ide==1)
    {
        spanpre.innerHTML = "<span style=\"font-weight:bold; font-family:Tahoma; font-size:9px; color:#B2B2B2\"><< Trước</span>";
    }
    else
    {
        spanpre.innerHTML = "<a style=\"font-weight:bold; font-family:Tahoma; font-size:9px; color:#C00\" id=\"aPre\" href=\"javascript:LoadPre();\"><< Trước</a>";
    }
}
//LoadEventsRelatedNews(_symbol,0,1,6);
GetALink(0);
</script>
                        
                            <!-- end -->
                            <div class="hosocongty">
                                
<style type="text/css">
.tabs4 li {margin-left: 5px;} .BanLanhDaoCoCuSoHuu_Sel {background-position: top center;}
</style>
<h2 class="cattitle noborder" id="taichinh">
    Hồ sơ công ty</h2>
<ul class="tabs4">
    <li id="liTabCongTy1CT"><a id="lsTab1CT" href="/upcom/A32/thong-tin-tai-chinh.chn" onclick="changeTabCongTy(1); return false;">Thông tin tài chính</a></li>
    <li id="liTabCongTy2CT"><a id="lsTab2CT" href="/upcom/A32/thong-tin-chung.chn" onclick="changeTabCongTy(2); return false;">Thông tin cơ bản</a></li>
    <li id="liTabCongTy3CT"><a id="lsTab3CT" href="/upcom/A32/ban-lanh-dao.chn" onclick="changeTabCongTy(3); return false;">Ban lãnh đạo và sở hữu </a></li>
    <li id="liTabCongTy4CT"><a id="lsTab4CT" href="/upcom/A32/cong-ty-con.chn" onclick="changeTabCongTy(4); return false;">Cty con &amp; liên kết</a></li>
    <li id="liTabCongTy5CT"><a id="lsTab5CT" href="/upcom/A32/bao-cao-tai-chinh.chn" onclick="javascript:changeTabCongTy(5); return false;">Tải BCTC</a></li>
</ul>
<div style="clear:both"></div>
<div class="phanchia clearfix">
    
    <div id="divStart" style="">
        
<div class="hosocongty">
    <div class="phanchia clearfix">
        <div class="l" style="cursor: pointer; padding: 5px 0;">
            <a id="idTabTaiChinhQuy" onclick="changeTabTaiChinh(1);">Theo quý</a> | <a id="idTabTaiChinhNam"
                class="active" onclick="changeTabTaiChinh(2);">Theo năm</a> | <a id="idTabTaiChinhSauThang"
                    onclick="changeTabTaiChinh(3);">Lũy kế 6 tháng</a>
        </div>
        <div class="r" style="cursor: pointer; padding: 5px 0;">
            <span>(1.000 VNĐ)</span>
        </div>
    </div>
    <div id="divHoSoCongTyAjax">
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
                <th class="col1">Chỉ tiêu &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<a onclick="ViewPage(1);" style="cursor: pointer; vertical-align: top;">
                    <img src="http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/Previous_Black.gif" id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_imgPre" alt="Xem dữ liệu trước" border="0" />&nbsp;Trước </a>&nbsp;&nbsp;&nbsp;&nbsp;<a onclick="ViewPage(-1);" style="cursor: pointer; vertical-align: top;">Sau&nbsp;<img src="http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/Next_Black.gif" id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_imgNext" alt="Xem dữ liệu tiếp" border="0" /></a>
                </th>
                <th align="center">
                    &nbsp;
                </th>
                <th align="center">
                    &nbsp;
                </th>
                <th align="center">
                    Năm 2017<br /><span style='color:#CC0000;'>(Đã kiểm toán)</span>
                </th>
                <th align="center">
                    Năm 2018<br /><span style='color:#CC0000;'>(Đã kiểm toán)</span>
                </th>
                <th align="right">Tăng trưởng
                </th>
            </tr>
            
                    <tr class="tbheader">
                        <td colspan="4" class="tbhl">
                            <div>
                                Kết quả kinh doanh 
                                <span style="color: #999999; font-weight: normal;">(1.000 VNĐ)</span>
                            </div>
                        </td>
                        <td colspan="2" style="font-weight: normal; text-align: right;">
                            <a href='/bao-cao-tai-chinh/A32/IncSta/2018/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-32.chn'><u>Xem đầy đủ</u></a>
                        </td>
                    </tr>
                    
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl00_rptData_ctl00_TrData" style="font-weight: normal; text-align: left;">
	<td class="col1">
                                    Doanh thu thuần về BH và cung cấp DV
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    611,910,105
                                </td>
	<td style="text-align: right">
                                    646,214,748
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 22px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl00_rptData_ctl01_TrData" style="font-weight: normal; text-align: left;background-color: #F6F6F6;">
	<td class="col1">
                                    Giá vốn hàng bán
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    546,258,715
                                </td>
	<td style="text-align: right">
                                    583,746,959
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 22px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl00_rptData_ctl02_TrData" style="font-weight: normal; text-align: left;">
	<td class="col1">
                                    Lợi nhuận gộp về BH và cung cấp DV
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    65,562,002
                                </td>
	<td style="text-align: right">
                                    62,447,820
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 22px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl00_rptData_ctl03_TrData" style="font-weight: normal; text-align: left;background-color: #F6F6F6;">
	<td class="col1">
                                    Lợi nhuận tài chính
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    13,094,214
                                </td>
	<td style="text-align: right">
                                    13,828,439
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 22px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl00_rptData_ctl04_TrData" style="font-weight: normal; text-align: left;">
	<td class="col1">
                                    Lợi nhuận khác
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    -111,857
                                </td>
	<td style="text-align: right">
                                    -391,704
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='top'><div style='overflow: hidden; background-color: #7f0102'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #cc0001'><img alt='' style='width: 4px;height: 6px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='top'><div style='overflow: hidden; background-color: #7f0102'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #cc0001'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl00_rptData_ctl05_TrData" style="font-weight: normal; text-align: left;background-color: #F6F6F6;">
	<td class="col1">
                                    Tổng lợi nhuận trước thuế
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    41,944,966
                                </td>
	<td style="text-align: right">
                                    51,500,795
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 19px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl00_rptData_ctl06_TrData" style="font-weight: normal; text-align: left;">
	<td class="col1">
                                    Lợi nhuận sau thuế
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    35,443,022
                                </td>
	<td style="text-align: right">
                                    43,095,884
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 19px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl00_rptData_ctl08_TrData" style="font-weight: normal; text-align: left;background-color: #F6F6F6;">
	<td class="col1">
                                    Lợi nhuận sau thuế của công ty mẹ
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    35,443,022
                                </td>
	<td style="text-align: right">
                                    43,095,884
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 19px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                    <tr><td colspan="6" style="text-align:center;">
                            <a href='/bao-cao-tai-chinh/A32/IncSta/2018/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-32.chn' style="display: block; padding: 5px; background-color: #F2F2F2; width: 150px; float: left; margin: 10px 10px 10px 250px;text-decoration:underline;">Xem đầy đủ</a>
                        </td>
                    </tr>
                    

<tr>
	<td>
	    <div style="font-weight:normal;padding:0 0 0 0" class="dltlonote">
	        <div style='float:left;padding-right:5px'><img alt='' src='http://images1.cafef.vn/batdongsan//Images/others/chart1.png' /></div>
	        <ul style="line-height:17px;padding-bottom:3px;">
	            <li>Lãi gộp từ HĐ SX-KD chính</li>
	            <li>Lãi gộp từ HĐ tài chính</li>
	            <li>Lãi gộp từ HĐ khác</li>
	        </ul>
	    </div>
	</td>
	<td align="right" style="padding-right:6px;"></td>
	<td align="right" "padding-right:6px;"></td>
	<td align="right" "padding-right:6px;"><img alt='' src='http://chart.apis.google.com/chart?chs=70x70&cht=p&chco=777BCC|BBCCED|0000006C&chd=t:'/></td>
	<td align="right" "padding-right:6px;"><img alt='' src='http://chart.apis.google.com/chart?chs=70x70&cht=p&chco=777BCC|BBCCED|0000006C&chd=t:'/></td>
	<td align="center"><div class="dltlonote">tỷ đồng</div></td>
</tr>

                    
                    
                    <tr class="tbheader">
                        <td colspan="4" class="tbhl">
                            <div>
                                Tài sản
                                <span style="color: #999999; font-weight: normal;">(1.000 VNĐ)</span>
                            </div>
                        </td>
                        <td colspan="2" style="font-weight: normal; text-align: right;">
                            <a href='/bao-cao-tai-chinh/A32/BSheet/2018/0/0/0/can-doi-ke-toan-cong-ty-co-phan-32.chn'><u>Xem đầy đủ</u></a>
                        </td>
                    </tr>
                    
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl01_rptData_ctl00_TrData" style="font-weight: normal; text-align: left;">
	<td class="col1">
                                    Tổng tài sản lưu động ngắn hạn
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    374,126,690
                                </td>
	<td style="text-align: right">
                                    335,863,031
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 21px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl01_rptData_ctl01_TrData" style="font-weight: normal; text-align: left;background-color: #F6F6F6;">
	<td class="col1">
                                    Tổng tài sản
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    500,992,328
                                </td>
	<td style="text-align: right">
                                    468,841,123
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 22px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl01_rptData_ctl02_TrData" style="font-weight: normal; text-align: left;">
	<td class="col1">
                                    Nợ ngắn hạn
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    322,279,644
                                </td>
	<td style="text-align: right">
                                    265,599,969
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 19px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl01_rptData_ctl03_TrData" style="font-weight: normal; text-align: left;background-color: #F6F6F6;">
	<td class="col1">
                                    Tổng nợ
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    324,709,022
                                </td>
	<td style="text-align: right">
                                    268,029,348
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 19px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                            <tr id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_rptNhomChiTieu_ctl01_rptData_ctl04_TrData" style="font-weight: normal; text-align: left;">
	<td class="col1">
                                    Vốn chủ sở hữu
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    &nbsp;
                                </td>
	<td style="text-align: right">
                                    176,283,306
                                </td>
	<td style="text-align: right">
                                    200,811,776
                                </td>
	<td style="text-align: right">
                                    <center><table class='BaoCaoTaiChinh_Chart' border='0' cellpadding='0' cellspacing='0' style='margin-top:3px;'><tr><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td><div style='overflow: hidden;'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 21px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><td><img alt='' style='width: 3px;' src='http://cafef3.vcmedia.vn/images/images/spacer.gif'/></td><td valign='bottom'><div style='overflow: hidden; background-color: #a4ccf0'><img alt='' style='width: 4px;height: 24px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div><div style='overflow: hidden; background-color: #5493be'><img alt='' style='width: 4px;height: 1px' src='http://cafef3.vcmedia.vn/images/images/spacer.gif' /></div></td><tr></table></center>
                                </td>
</tr>

                        
                    <tr><td colspan="6" style="text-align:center;">
                            <a href='/bao-cao-tai-chinh/A32/BSheet/2018/0/0/0/can-doi-ke-toan-cong-ty-co-phan-32.chn' style="display: block; padding: 5px; background-color: #F2F2F2; width: 150px; float: left; margin: 10px 10px 10px 250px;text-decoration:underline;">Xem đầy đủ</a>
                        </td>
                    </tr>
                    
                    
                    
        </table>

        
        <div style="display: none" id="HSCTLoaded">
        </div>
    </div>
    <div class="chisokhac">
        <ul>
            <li class="csk active" id="li_cstc">Chỉ số tài chính</li>
            <li class="csk" id="li_ctkh">Chỉ tiêu kế hoạch</li>
        </ul>

        <div class="financial">
            <table>
                <thead>
                    <tr>
                        <th>Chỉ tiêu tài chính 
                                
                                <a href="javascript:void(0)" id="a_prev">
                                    <img src="http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/Previous_Red.gif" style="vertical-align: middle; margin-bottom: 2px; margin-left: 5px;" />
                                    Trước</a>
                            <a href="javascript:void(0)" id="a_next">Sau
                                <img src="http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/Next_Black.gif" style="vertical-align: middle; vertical-align: middle; margin-bottom: 2px;" /></a> </th>
                        <th id="th1" class="data"></th>
                        <th id="th2" class="data"></th>
                        <th id="th3" class="data"></th>
                        <th id="th4" class="data"></th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            <label title="Lợi nhuận trên mỗi cổ phiếu (EPS -Earning Per Share)">
                                EPS (nghìn đồng)</label>
                        </td>
                        <td class="data" id="eps_td1"></td>
                        <td class="data" id="eps_td2"></td>
                        <td class="data" id="eps_td3"></td>
                        <td class="data" id="eps_td4"></td>
                        <td id="eps_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label title="Giá trị sổ sách (BV - Book value)">
                                BV (nghìn đồng)</label>
                        </td>
                        <td class="data" id="bv_td1"></td>
                        <td class="data" id="bv_td2"></td>
                        <td class="data" id="bv_td3"></td>
                        <td class="data" id="bv_td4"></td>
                        <td id="bv_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label>P/E</label>
                        </td>
                        <td class="data" id="pe_td1"></td>
                        <td class="data" id="pe_td2"></td>
                        <td class="data" id="pe_td3"></td>
                        <td class="data" id="pe_td4"></td>
                        <td id="pe_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label title="Tỷ suất sinh lời trên tổng tài sản (ROA – Return on Total Asset)">
                                ROA (%)</label>
                        </td>
                        <td class="data" id="roa_td1"></td>
                        <td class="data" id="roa_td2"></td>
                        <td class="data" id="roa_td3"></td>
                        <td class="data" id="roa_td4"></td>
                        <td id="roa_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label title="Tỷ suất sinh lời trên vốn chủ sở hữu (ROE – Return on Equity)">
                                ROE (%)</label>
                        </td>
                        <td class="data" id="roe_td1"></td>
                        <td class="data" id="roe_td2"></td>
                        <td class="data" id="roe_td3"></td>
                        <td class="data" id="roe_td4"></td>
                        <td id="roe_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label title="Tỷ suất sinh lợi trên doanh thu thuần (ROS -Return on sales)">
                                ROS (%)</label>
                        </td>
                        <td class="data" id="ros_td1"></td>
                        <td class="data" id="ros_td2"></td>
                        <td class="data" id="ros_td3"></td>
                        <td class="data" id="ros_td4"></td>
                        <td id="ros_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label title="Tỷ suất lợi nhuận gộp">
                                GOS (%)</label>
                        </td>
                        <td class="data" id="gos_td1"></td>
                        <td class="data" id="gos_td2"></td>
                        <td class="data" id="gos_td3"></td>
                        <td class="data" id="gos_td4"></td>
                        <td id="gos_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label title="Tỷ lệ nợ / tài sản">
                                DAR (%)</label>
                        </td>
                        <td class="data" id="dar_td1"></td>
                        <td class="data" id="dar_td2"></td>
                        <td class="data" id="dar_td3"></td>
                        <td class="data" id="dar_td4"></td>
                        <td id="dar_td5" class="chart"></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="khkd hidden">
            <table>
                <thead>
                    <tr>
                        <th>Kế hoạch kinh doanh <a href="javascript:void(0)" id="a_kh_prev">
                            <img src="http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/Previous_Red.gif" style="vertical-align: middle; margin-bottom: 2px; margin-left: 5px;" />
                            Trước</a><a href="javascript:void(0)" id="a_kh_next">Sau 
                                <img src="http://cafef3.vcmedia.vn/images/Scontrols/Images/LSG/Next_Black.gif" style="vertical-align: middle; vertical-align: middle; margin-bottom: 2px;" /></a> </th>
                        <th id="th_kh1" class="data"></th>
                        <th id="th_kh2" class="data"></th>
                        <th id="th_kh3" class="data"></th>
                        <th id="th_kh4" class="data"></th>
                        <th>&nbsp;</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            <label>Tổng doanh thu</label>
                        </td>
                        <td class="data" id="tdt_td1"></td>
                        <td class="data" id="tdt_td2"></td>
                        <td class="data" id="tdt_td3"></td>
                        <td class="data" id="tdt_td4"></td>
                        <td id="tdt_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label>Lợi nhuận trước thuế</label>
                        </td>
                        <td class="data" id="lntt_td1"></td>
                        <td class="data" id="lntt_td2"></td>
                        <td class="data" id="lntt_td3"></td>
                        <td class="data" id="lntt_td4"></td>
                        <td id="lntt_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label>Lợi nhuận sau thuế</label>
                        </td>
                        <td class="data" id="lnst_td1"></td>
                        <td class="data" id="lnst_td2"></td>
                        <td class="data" id="lnst_td3"></td>
                        <td class="data" id="lnst_td4"></td>
                        <td id="lnst_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label>Tỷ lệ cổ tức bằng tiền</label>
                        </td>
                        <td class="data" id="ctbt_td1"></td>
                        <td class="data" id="ctbt_td2"></td>
                        <td class="data" id="ctbt_td3"></td>
                        <td class="data" id="ctbt_td4"></td>
                        <td id="ctbt_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label>Tỷ lệ cổ tức bằng cổ phiếu</label>
                        </td>
                        <td class="data" id="ctbcp_td1"></td>
                        <td class="data" id="ctbcp_td2"></td>
                        <td class="data" id="ctbcp_td3"></td>
                        <td class="data" id="ctbcp_td4"></td>
                        <td id="ctbcp_td5" class="chart"></td>
                    </tr>
                    <tr>
                        <td>
                            <label>Tăng vốn (%)</label>
                        </td>
                        <td class="data" id="tv_td1"></td>
                        <td class="data" id="tv_td2"></td>
                        <td class="data" id="tv_td3"></td>
                        <td class="data" id="tv_td4"></td>
                        <td id="tv_td5" class="chart"></td>
                    </tr>
                </tbody>
            </table>

        </div>
    </div>

    <div id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_divHieuQua">
        <table>
            <tr class="tbheader">
                <td class="tbhl">
                    <div>
                        Đánh giá hiệu quả
                    </div>
                </td>
            </tr>
        </table>
        <div class="phanchia clearfix">
            <div style="cursor: pointer; padding: 5px 0; float: none;" class="l">
                <a id="idTabTaiChinhQuy1" onclick="changeTabTaiChinh1(1);">4 quý gần nhất</a> |
                <a id="idTabTaiChinhNam1" class="active" onclick="changeTabTaiChinh1(2);">4 năm gần
                    nhất</a> | <a id="idTabTaiChinhSauThang1" onclick="changeTabTaiChinh1(3);">Lũy kế 6
                        tháng</a>
            </div>
        </div>
        <div id="divChartBCTC">
            
<div style="text-align:center;padding-bottom:10px;">
<img id = "img_A32" alt='' src='http://chart.apis.google.com/chart?chxl=0:|2017|2018|2:|0%|6.8%|8.5%|10.3%|12%&chxr=1,0,600&chxt=x,y,r&chbh=a&chs=205x130&cht=bvg&chco=4D89F9,C6D9FD,926BDA&chds=0,600,0,600,0,12&chd=t2:500.992328357,468.841123434|35.443022026,43.095883812|7.07,9.19&chdlp=b&chg=0,25&chxs=0,676767,10,0,l,676767|1,676767,10,0,l,676767|2,676767,10,0,l,676767|3,676767,10,0,l,676767&chm=D,926BDA,2,-1,3|s,6000A7,2,-1,5'/>
<img id = "img_A32" alt='' src='http://chart.apis.google.com/chart?chxl=0:|2017|2018|2:|0%|18.5%|21%|23.5%|26%&chxr=1,0,300&chxt=x,y,r&chbh=a&chs=205x130&cht=bvg&chco=4D89F9,C6D9FD,926BDA&chds=0,300,0,300,0,26&chd=t2:176.283306329,200.811775837|35.443022026,43.095883812|20.11,21.46&chdlp=b&chg=0,25&chxs=0,676767,10,0,l,676767|1,676767,10,0,l,676767|2,676767,10,0,l,676767|3,676767,10,0,l,676767&chm=D,926BDA,2,-1,3|s,6000A7,2,-1,5'/>
<div><div style='padding-left:165px;float:left;width:180px;text-align:left;padding-bottom:10px;'><div style='float:left;padding-right:5px'><img alt='' src='http://images1.cafef.vn/batdongsan//Images/others/legend.png'></div><div style='font-weight:normal;padding:0 0 0 0;text-align:left;' class='dltlonote'><ul style='line-height:1.6em;'><li>Tổng tài sản</li><li>LN ròng</li><li>ROA (%)</li></ul></div></div><div style='padding-left:45px;float:left;width:220px;text-align:left;'><div style='float:left;padding-right:5px'><img alt='' src='http://images1.cafef.vn/batdongsan//Images/others/legend.png'></div><div style='font-weight:normal;padding:0 0 0 0;text-align:left;' class='dltlonote'><ul style='line-height:1.6em;'><li>Vốn chủ sở hữu</li><li>LN ròng</li><li>ROE (%)</li></ul></div></div></div>
</div>
            
<div style="background:#ffffff;float:left" class="DuLieu_ChartBCTC">
<img class="img_bctc_A32" alt='' src='http://chart.apis.google.com/chart?chxl=0:|2017|2018|2:|0%|25%|50%|75%|100%&chxr=1,0,700&chxt=x,y,r&chbh=a&chs=205x130&cht=bvg&chco=4D89F9,C6D9FD,926BDA&chds=0,700,0,700,0,100&chd=t2:611.910105351,646.214747621|35.443022026,43.095883812|5.79,6.67&chdlp=b&chg=0,25&chxs=0,676767,10,0,l,676767|1,676767,10,0,l,676767|2,676767,10,0,l,676767|3,676767,10,0,l,676767&chm=D,926BDA,2,-1,3|s,6000A7,2,-1,5'/>
<img class="img_bctc_A32" alt='' src='http://chart.apis.google.com/chart?chxl=0:|2017|2018|2:|0%|25%|50%|75%|100%&chxr=1,0,700&chxt=x,y,r&chbh=a&chs=205x130&cht=bvg&chco=4D89F9,C6D9FD,926BDA&chds=0,700,0,700,0,100&chd=t2:611.820717623,646.194779056|65.562002461,62.447819899|10.72,9.66&chdlp=b&chg=0,25&chxs=0,676767,10,0,l,676767|1,676767,10,0,l,676767|2,676767,10,0,l,676767|3,676767,10,0,l,676767&chm=D,926BDA,2,-1,3|s,6000A7,2,-1,5'/>
<img class="img_bctc_A32" alt='' src='http://chart.apis.google.com/chart?chxl=0:|2017|2018|2:|0%|25%|50%|75%|100%&chxr=1,0,600&chxt=x,y,r&chbh=a&chs=205x130&cht=bvg&chco=4D89F9,C6D9FD,926BDA&chds=0,600,0,600,0,100&chd=t2:500.992328357,468.841123434|324.709022028,268.029347597|64.81,57.17&chdlp=b&chg=0,25&chxs=0,676767,10,0,l,676767|1,676767,10,0,l,676767|2,676767,10,0,l,676767|3,676767,10,0,l,676767&chm=D,926BDA,2,-1,3|s,6000A7,2,-1,5'/>
<div><div style='padding-left:45px;float:left;width:180px;'><div style='float:left;padding-right:5px'><img alt='' src='http://images1.cafef.vn/batdongsan//Images/others/legend.png'></div><div style='font-weight:normal;padding:0 0 0 0' class='dltlonote'><ul style='line-height:1.6em;'><li>Tổng thu</li><li>LN ròng</li><li>Tỷ suất LN ròng (%)</li></ul></div></div><div style='padding-left:45px;float:left;width:220px;'><div style='float:left;padding-right:5px'><img alt='' src='http://images1.cafef.vn/batdongsan//Images/others/legend.png'></div><div style='font-weight:normal;padding:0 0 0 0' class='dltlonote'><ul style='line-height:1.6em;'><li>DThu thuần</li><li>LN gộp</li><li>Tỷ suất LN gộp (%)</li></ul></div></div><div style='padding-left:45px;'><div style='float:left;padding-right:5px'><img alt='' src='http://images1.cafef.vn/batdongsan//Images/others/legend.png'></div><div style='font-weight:normal;padding:0 0 0 0' class='dltlonote'><ul style='line-height:1.6em;'><li>Tổng tài sản</li><li>Tổng nợ</li><li>Nợ/tài sản (%)</li></ul></div></div></div>
</div>

            <div style="width: 160px; float: left; padding-left: 30px;" class="dltlonote">
                Đơn vị: tỷ đồng
            </div>
        </div>
    </div>
    
</div>
<input name="ctl00$ContentPlaceHolder1$CompanyInfo$FinanceStatement1$txtIdx" type="hidden" id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_txtIdx" value="0" />
<input name="ctl00$ContentPlaceHolder1$CompanyInfo$FinanceStatement1$txtType" type="hidden" id="ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_txtType" value="2" />

<script language="javascript" type="text/javascript">
    function changeTabTaiChinh(index) {
        var txtType = document.getElementById('ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_txtType');
        txtType.value = index;
        var txtIdx = document.getElementById('ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_txtIdx');
        txtIdx.value = "0";

        var idTabTaiChinhQuy = document.getElementById('idTabTaiChinhQuy');
        var idTabTaiChinhNam = document.getElementById('idTabTaiChinhNam');
        var idTabTaiChinhSauThang = document.getElementById('idTabTaiChinhSauThang');
        if (index == 1) {
            idTabTaiChinhQuy.className = "active";
            idTabTaiChinhNam.className = ""; idTabTaiChinhSauThang.className = "";
        }
        else if (index == 2) {
            idTabTaiChinhQuy.className = ""; idTabTaiChinhSauThang.className = "";
            idTabTaiChinhNam.className = "active";
        } else {
            idTabTaiChinhQuy.className = ""; idTabTaiChinhSauThang.className = "active";
            idTabTaiChinhNam.className = "";
        }
        LoadHoSoCongTy('A32', index, txtIdx.value, 4);
    }

    function changeTabTaiChinh1(index) {
        var txtType = document.getElementById('ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_txtType');
        txtType.value = index;
        var txtIdx = document.getElementById('ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_txtIdx');
        txtIdx.value = "0";

        var idTabTaiChinhQuy1 = document.getElementById('idTabTaiChinhQuy1');
        var idTabTaiChinhNam1 = document.getElementById('idTabTaiChinhNam1');
        var idTabTaiChinhSauThang1 = document.getElementById('idTabTaiChinhSauThang1');
        if (index == 1) {
            idTabTaiChinhQuy1.className = "active";
            idTabTaiChinhNam1.className = ""; idTabTaiChinhSauThang1.className = "";
        }
        else if (index == 2) {
            idTabTaiChinhQuy1.className = ""; idTabTaiChinhSauThang1.className = "";
            idTabTaiChinhNam1.className = "active";
        } else {
            idTabTaiChinhQuy1.className = ""; idTabTaiChinhSauThang1.className = "active";
            idTabTaiChinhNam1.className = "";
        }
        LoadHoSoCongTy1('A32', index, txtIdx.value, 4);
    }

    function ViewPage(index) {
        var txtIdx = document.getElementById('ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_txtIdx');
        var currIdx = parseInt(txtIdx.value) + parseInt(index);
        if (currIdx < 0) return;
        var item = '2';
        var txtType = document.getElementById('ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_txtType');
        if (txtType.value == "2")
            item = '1';
        //if ((currIdx)*4 > item) return; 
        txtIdx.value = currIdx;


        LoadHoSoCongTy('A32', txtType.value, txtIdx.value, 4);
    }

    function LoadHoSoCongTy(symbol, type, index, size) {
        var html = $('#HSCTLoaded_Type' + type + "_Page" + index).html();
        if (html != null && html != '') {
            $('#divHoSoCongTyAjax').html(html);
        }
        else {
            $.ajax({
                type: "GET",
                url: "/Ajax/HoSoCongTy.aspx",
                data: "symbol=" + _symbol + "&Type=" + type + "&PageIndex=" + index + "&PageSize=" + size,
                success: function (msg) {
                    document.getElementById("divHoSoCongTyAjax").innerHTML = msg;
                    $('#HSCTLoaded').html($('#HSCTLoaded').html() + "<div id='HSCTLoaded_Type" + type + "_Page" + index + "'>" + msg + "</div>");
                }
            });
        }

    }

    function LoadHoSoCongTy1(symbol, type, index, size) {
        $.ajax({
            type: "GET",
            url: "/Ajax/BCTCChart.aspx",
            data: "symbol=" + _symbol + "&Type=" + type + "&PageIndex=" + index + "&PageSize=" + size,
            success: function (msg) {
                document.getElementById("divChartBCTC").innerHTML = msg;
            }
        });

    }
    if (document.getElementById("ctl00_ContentPlaceHolder1_CompanyInfo_FinanceStatement1_txtType").value == '1') {
        $('#idTabTaiChinhQuy').addClass('active');
        $('#idTabTaiChinhNam').removeClass('active');
        $('#idTabTaiChinhQuy1').addClass('active');
        $('#idTabTaiChinhNam1').removeClass('active');
    }
</script>

<script src="http://cafef3.vcmedia.vn/v3/js/financestatement.min.1.5.js"></script>
<link href="http://cafef3.vcmedia.vn/v3/styles/indicators.min.1.1.css" rel="stylesheet" />
    </div>
    <div id="divStart2" style="display:none;">
        
        
        
        
        
    </div>
    <div id="divAjax" align="center" style="overflow: hidden; padding-top: 6px; display: none">
        <div id="loading">
            <img src="http://cafef3.vcmedia.vn/v2/images/loading.gif" alt="" />
        </div>
    </div>
</div>


<script type="text/javascript">
    var strThongTinChung = ""; var strBanLanhDaoVaSoHuu = ""; var strCongTyCon = ""; var strBaoCaoTaiChinh = ""; var divStart = document.getElementById("divStart"); var divAjax = document.getElementById("divAjax"); var tab1CT = document.getElementById("lsTab1CT"); var tab2CT = document.getElementById("lsTab2CT"); var tab3CT = document.getElementById("lsTab3CT"); var tab4CT = document.getElementById("lsTab4CT"); var tab5CT = document.getElementById("lsTab5CT"); var liTabCongTy1CT = document.getElementById("liTabCongTy1CT"); var liTabCongTy2CT = document.getElementById("liTabCongTy2CT"); var liTabCongTy3CT = document.getElementById("liTabCongTy3CT"); var liTabCongTy4CT = document.getElementById("liTabCongTy4CT"); var liTabCongTy5CT = document.getElementById("liTabCongTy5CT"); var sym = 'A32'; divAjax.style.display = "none"; 
    var currenttab = '1';
    $(document).ready(function(e) {
        //if(currenttab!=0) {changeTabCongTy(currenttab);}
        $('#liTabCongTy'+currenttab+'CT').addClass('active');
        $('#liTabCongTy'+currenttab+'CT a').css('color','#C00');
    });
    function LoadDocument(type, year)
    {
        $.ajax({
	        type: "GET",
	        url: "/Ajax/CongTy/BaoCaoTaiChinh.aspx",
	        data: "sym=" + 'A32' + "&type=" + type + "&year=" + year,
	        success: function(msg){
	             document.getElementById('divDocument').innerHTML=msg;
	        }
        });
    }
</script>


                                <!-- // Hồ sơ công ty -->
                            </div>
                            <div>
                                
                            </div>
                            

                        </div>
                    </div>
                    <!-- //column 1 -->
                    <div id="sidebar">
                        <!-- //search -->
                        
 
<div id="CafeF_BoxSearch"></div>
                        
                        <!-- //End -->
                        <!-- //lichsu giao dich -->
                        
    <style type="text/css">
        .lichsu .col2 {white-space:nowrap;}
        .lichsu .col3 {
            text-align:right;
        }
        .lichsu .col4{width:inherit !important}
        .lichsu td {padding:4px 4px 4px 2px !important;}
        .lichsu td .pink{color: #FF00FF !important;}
        .lichsu td .blue{color: #006699 !important;}
        
    </style>
<div class="lichsu">
    <ul class="tabs3">
        <li id="lstab1" ><a id=aLSGD href="javascript:changeTabLichSu(1);" style="color:#cc0000;">Lịch sử GD</a></li>
        <li id="lstab2"><a id=aTKDL href="javascript:changeTabLichSu(2);">TK Đặt lệnh</a></li>
        <li id="lstab3"><a id=aNDTNN href="javascript:changeTabLichSu(3);">NĐTNN</a></li>
    </ul>
    <div style="clear:both"></div>
    <div id='divData1LichSu'>
    <table width="100%" border="0" cellspacing="0" cellpadding="0">
        <tr>
          <th class="col1">Ngày</th>
          <th class="col2">Thay đổi giá</th>
          <th class="col3">KL khớp lệnh</th>
          <th class="col4">Tổng GTGD</th>
        </tr>
        
                 <tr class="even">
                    <td class="col1">27/09</td>
                    <td class="col2"><div class="l">27</div><div class='r up green'>3.40 (14.40%)</div></td>
                    <td class="col3">1,100</td>
                    <td class="col4">29,700</td>
                </tr>
            
                <tr class="odd">
                    <td class="col1">26/09</td>
                    <td class="col2"><div class="l">23.6</div><div class='r nochange orange'>0.00 (0.00%)</div></td>
                    <td class="col3">0</td>
                    <td class="col4">0</td>
                </tr>
            
                 <tr class="even">
                    <td class="col1">25/09</td>
                    <td class="col2"><div class="l">23.6</div><div class='r nochange orange'>0.00 (0.00%)</div></td>
                    <td class="col3">400</td>
                    <td class="col4">9,450</td>
                </tr>
            
                <tr class="odd">
                    <td class="col1">24/09</td>
                    <td class="col2"><div class="l">23.6</div><div class='r nochange orange'>0.00 (0.00%)</div></td>
                    <td class="col3">0</td>
                    <td class="col4">0</td>
                </tr>
            
                 <tr class="even">
                    <td class="col1">23/09</td>
                    <td class="col2"><div class="l">23.6</div><div class='r nochange orange'>0.00 (0.00%)</div></td>
                    <td class="col3">0</td>
                    <td class="col4">0</td>
                </tr>
            
                <tr class="odd">
                    <td class="col1">20/09</td>
                    <td class="col2"><div class="l">23.5</div><div class='r down red'>-0.70 (-2.90%)</div></td>
                    <td class="col3">3,600</td>
                    <td class="col4">85,020</td>
                </tr>
            
                 <tr class="even">
                    <td class="col1">19/09</td>
                    <td class="col2"><div class="l">24.2</div><div class='r nochange orange'>0.00 (0.00%)</div></td>
                    <td class="col3">100</td>
                    <td class="col4">2,420</td>
                </tr>
            
                <tr class="odd">
                    <td class="col1">18/09</td>
                    <td class="col2"><div class="l">24.2</div><div class='r down red'>-3.30 (-12.00%)</div></td>
                    <td class="col3">2,600</td>
                    <td class="col4">62,920</td>
                </tr>
            
                 <tr class="even">
                    <td class="col1">17/09</td>
                    <td class="col2"><div class="l">27.5</div><div class='r up green'>1.30 (5.00%)</div></td>
                    <td class="col3">100</td>
                    <td class="col4">2,750</td>
                </tr>
            
                <tr class="odd">
                    <td class="col1">16/09</td>
                    <td class="col2"><div class="l">26.2</div><div class='r nochange orange'>0.00 (0.00%)</div></td>
                    <td class="col3">0</td>
                    <td class="col4">0</td>
                </tr>
                
	</table>
	 <div class="xemtiep clearfix">
  	    <a target="_blank" href='/Lich-su-giao-dich-A32-1.chn'>Xem tất cả</a>
        <div class="donvigtgd">Đơn vị GTGD: 1000 VNĐ </div>
    </div>
	</div>
	<div id="divData2LichSu" align="center" style="overflow: hidden; padding-top: 6px; display:none">
	    <div id="loading"><img src="/images/loading.gif" /></div>
    </div>
</div>
<script language="javascript" type="text/javascript">
    var sym = 'A32';
    var strNDTNNN = ""; var strKLDT = ""; var divData1LichSu = document.getElementById("divData1LichSu"); var divData2LichSu = document.getElementById("divData2LichSu"); var tab1LichSu = document.getElementById("aLSGD"); var tab2LichSu = document.getElementById("aTKDL"); var tab3LichSu = document.getElementById("aNDTNN"); divData2LichSu.style.display = "none"; tab1LichSu.style.color = "#cc0000";
 </script>


                        <!-- end-->
                        <!-- //Kế hoạch kinh doanh -->
                        
<style type="text/css">
.kehoachkd .tooltip li {background: none;list-style: disc inside;}
</style>
<div class="kehoachkd">
<h3 class="cattitle noborder">KẾ HOẠCH KINH DOANH NĂM 2019</h3>

    <ul>
        <li class="clearfix">
            <div class="l">Doanh thu</div>
            <div class="r">675.76 tỷ</div>
        </li>
        <li class="clearfix">
            <div class="l">Lợi nhuận trước thuế</div>
            <div class="r">43.96 tỷ</div>
        </li>
        <li class="clearfix">
            <div class="l">Lợi nhuận sau thuế</div>
            <div class="r">N/A</div>
        </li>
        <li class="clearfix">
            <div class="l">Cổ tức bằng tiền mặt</div>
            <div class="r">20 %</div>
        </li>
        <li class="clearfix">
            <div class="l">Cổ tức bằng cổ phiếu</div>
            <div class="r">N/A</div>
        </li>
        <li class="clearfix">
            <div class="l">Dự kiến tăng vốn lên</div>
            <div class="r">N/A</div>
        </li>
    </ul>


    <div class="xemtiep"><a href="javascript:void(0);" class="tt" style="color:#003366">Xem chi tiết<span class="tooltip"><span class="top"></span><span class="middle"><strong>Chi tiết phương án kinh doanh năm 2019</strong><br /></span><span class="bottom"></span></span></a></div>
</div>
                        <!-- end-->
                        <!-- //Báo cáo phân tích -->
                        <div id="ctl00_ContentPlaceHolder1_ucAnalyseReports_divCompany" class="baocaophantich">
<h3 class="cattitle noborder">BÁO CÁO PHÂN TÍCH</h3>
    
            <ul>
        
            <li>
                <div><a href="/phan-tich-bao-cao2481.chn">Báo cáo Kinh tế tài chính tháng 11/2013 - CafeF&nbsp;</a>(14/12/2013)</div>
            </li>
        
            </ul>
            
    <div class="xemtiep"><a href="/phan-tich-bao-cao.chn">Xem tiếp</a></div>
</div>
                        <!-- end-->
                        <!-- // Công ty cùng ngành -->
                        
        <div class="congtycungnganh">
            <h3>CTY CÙNG NGÀNH <span class="subtitle" style="color:Red;">Hàng tiêu dùng / Da giầy</span></h3>
            
                <div id="ctl00_ContentPlaceHolder1_ucInSameCategory_tblCTCNsv">
                <div id="tblCTCN">
            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                <tr>
                    <th>Mã CK</th>
                     <th>Sàn</th>
                    <th>&nbsp;</th>
                    <th>Giá</th>
                    <th>EPS</th>
                    <th>P/E</th>
                </tr>                
                
                        <tr class="even">
                            <td class="col1"><a title='C&#244;ng ty Cổ phần Đầu tư Nh&#227;n hiệu Việt' href='http://s.cafef.vn/upcom/ABR-cong-ty-co-phan-dau-tu-nhan-hieu-viet.chn'>ABR</a></td>
                            <td class="col1">Upcom</td>
                            <td class="col2">22.0</td>
                            <td class="col3"><div id="ctl00_ContentPlaceHolder1_ucInSameCategory_rptSameCategory_ctl00_divColor" class="orange">(+0.0%)</div></td>
                            <td class="col4">0.3</td>
                            <td class="col5">87.2</td>
                        </tr>
                    
                        <tr class="odd">
                            <td class="col1"><a title='C&#244;ng ty Cổ phần N&#244;ng L&#226;m Nghiệp B&#236;nh Dương' href='http://s.cafef.vn/upcom/AFC-cong-ty-co-phan-nong-lam-nghiep-binh-duong.chn'>AFC</a></td>
                            <td class="col1">Upcom</td>
                            <td class="col2">10.0</td>
                            <td class="col3"><div id="ctl00_ContentPlaceHolder1_ucInSameCategory_rptSameCategory_ctl01_divColor" class="orange">(+0.0%)</div></td>
                            <td class="col4">-0.2</td>
                            <td class="col5">-51.7</td>
                        </tr>
                    
                        <tr class="even">
                            <td class="col1"><a title='Tr&#225;i Phiếu C&#244;ng ty Cổ phần Dinh dưỡng N&#244;ng nghiệp Quốc tế' href='http://s.cafef.vn/hose/ANC11601-trai-phieu-cong-ty-co-phan-dinh-duong-nong-nghiep-quoc-te.chn'>ANC11601</a></td>
                            <td class="col1">HSX</td>
                            <td class="col2">-</td>
                            <td class="col3"><div id="ctl00_ContentPlaceHolder1_ucInSameCategory_rptSameCategory_ctl02_divColor">-</div></td>
                            <td class="col4">59.1</td>
                            <td class="col5">-</td>
                        </tr>
                    
                        <tr class="odd">
                            <td class="col1"><a title='CTCP Cơ kh&#237; v&#224; Thiết bị &#225;p lực - VVMI' href='http://s.cafef.vn/upcom/APL-ctcp-co-khi-va-thiet-bi-ap-luc-vvmi.chn'>APL</a></td>
                            <td class="col1">Upcom</td>
                            <td class="col2">14.0</td>
                            <td class="col3"><div id="ctl00_ContentPlaceHolder1_ucInSameCategory_rptSameCategory_ctl03_divColor" class="orange">(+0.0%)</div></td>
                            <td class="col4">2.0</td>
                            <td class="col5">7.1</td>
                        </tr>
                    
                        <tr class="even">
                            <td class="col1"><a title='Ng&#226;n h&#224;ng Thương mại cổ phần Bắc &#193;' href='http://s.cafef.vn/upcom/BAB-ngan-hang-thuong-mai-co-phan-bac-a.chn'>BAB</a></td>
                            <td class="col1">Upcom</td>
                            <td class="col2">17.9</td>
                            <td class="col3"><div id="ctl00_ContentPlaceHolder1_ucInSameCategory_rptSameCategory_ctl04_divColor" class="green">(+0.6%)</div></td>
                            <td class="col4">1.2</td>
                            <td class="col5">14.6</td>
                        </tr>
                    
                        <tr class="odd">
                            <td class="col1"><a title='C&#244;ng ty cổ phần Bao b&#236; Bia – Rượu – Nước giải kh&#225;t' href='http://s.cafef.vn/upcom/BAL-cong-ty-co-phan-bao-bi-bia-ruou-nuoc-giai-khat.chn'>BAL</a></td>
                            <td class="col1">Upcom</td>
                            <td class="col2">8.3</td>
                            <td class="col3"><div id="ctl00_ContentPlaceHolder1_ucInSameCategory_rptSameCategory_ctl05_divColor" class="red">(-9.8%)</div></td>
                            <td class="col4">2.1</td>
                            <td class="col5">4.0</td>
                        </tr>
                    
                        <tr class="even">
                            <td class="col1"><a title='Tổng C&#244;ng ty Đầu tư v&#224; ph&#225;t triển C&#244;ng nghiệp - CTCP' href='http://s.cafef.vn/upcom/BCM-tong-cong-ty-dau-tu-va-phat-trien-cong-nghiep-ctcp.chn'>BCM</a></td>
                            <td class="col1">Upcom</td>
                            <td class="col2">31.5</td>
                            <td class="col3"><div id="ctl00_ContentPlaceHolder1_ucInSameCategory_rptSameCategory_ctl06_divColor" class="green">(+0.3%)</div></td>
                            <td class="col4">1.2</td>
                            <td class="col5">26.7</td>
                        </tr>
                    
                        <tr class="odd">
                            <td class="col1"><a title='Tổng C&#244;ng ty X&#226;y dựng Bạch Đằng' href='http://s.cafef.vn/upcom/BDC-tong-cong-ty-xay-dung-bach-dang.chn'>BDC</a></td>
                            <td class="col1">Upcom</td>
                            <td class="col2">13.0</td>
                            <td class="col3"><div id="ctl00_ContentPlaceHolder1_ucInSameCategory_rptSameCategory_ctl07_divColor" class="green">(+11.1%)</div></td>
                            <td class="col4">0.6</td>
                            <td class="col5">23.1</td>
                        </tr>
                    
                        <tr class="even">
                            <td class="col1"><a title='CTCP May mặc B&#236;nh Dương' href='http://s.cafef.vn/upcom/BDG-ctcp-may-mac-binh-duong.chn'>BDG</a></td>
                            <td class="col1">Upcom</td>
                            <td class="col2">33.2</td>
                            <td class="col3"><div id="ctl00_ContentPlaceHolder1_ucInSameCategory_rptSameCategory_ctl08_divColor" class="orange">(+0.0%)</div></td>
                            <td class="col4">9.6</td>
                            <td class="col5">3.5</td>
                        </tr>
                    
                        <tr class="odd">
                            <td class="col1"><a title='CTCP Điện tử Bi&#234;n H&#242;a' href='http://s.cafef.vn/upcom/BEL-ctcp-dien-tu-bien-hoa.chn'>BEL</a></td>
                            <td class="col1">Upcom</td>
                            <td class="col2">14.2</td>
                            <td class="col3"><div id="ctl00_ContentPlaceHolder1_ucInSameCategory_rptSameCategory_ctl09_divColor" class="orange">(+0.0%)</div></td>
                            <td class="col4">-0.1</td>
                            <td class="col5">-154.9</td>
                        </tr>
                                   
            </table>
            </div>
            </div>
            <div id="ctl00_ContentPlaceHolder1_ucInSameCategory_paging" class="paging"><a style='padding-left=5px' href='javascript:void(0);' rel='prev'>&lt;</a>&nbsp;<a href='javascript:void(0);' rel='1' class='current'>1</a>&nbsp;<a href='javascript:void(0);' rel='2'>2</a>&nbsp;<a href='javascript:void(0);' rel='3'>3</a>&nbsp;<a href='javascript:void(0);' rel='4'>4</a>&nbsp;<a href='javascript:void(0);' rel='5'>5</a>&nbsp;<a href='javascript:void(0);' rel='6'>6</a>&nbsp;<a href='javascript:void(0);' rel='7'>7</a>&nbsp;<a href='javascript:void(0);' rel='8'>8</a>&nbsp;<a href='javascript:void(0);' rel='9'>9</a>&nbsp;<a href='javascript:void(0);' rel='10'>10</a>&nbsp;<a href='javascript:void(0);' rel='11'>11</a>&nbsp;<a href='javascript:void(0);' rel='12'>12</a>&nbsp;<a href='javascript:void(0);' rel='13'>13</a>&nbsp;<a href='javascript:void(0);' rel='14'>14</a>&nbsp;<a href='javascript:void(0);' rel='15'>15</a>&nbsp;<a href='javascript:void(0);' rel='16'>16</a>&nbsp;<a href='javascript:void(0);' rel='17'>17</a>&nbsp;<a href='javascript:void(0);' rel='18'>18</a>&nbsp;<a href='javascript:void(0);' rel='19'>19</a>&nbsp;<a href='javascript:void(0);' rel='next'>&gt;</a>&nbsp;</div>
             <div class="pagingnote" id="pagingnote">Trang 1/19</div>
        </div><input type="hidden" id="txtIdxSameCategory" value="1" />
<script language="javascript" type="text/javascript">
var symbol = 'A32';
var TotalPage = '19';
//document.getElementById('txtIdxSameCategory').value = '1'; 
</script>



                        <!-- End-->
                        <!-- EPS, P/E tương đương -->
                        

<div class="epspe">
    <ul class="tabs3">
        <li><a id="lstab1EPS" style="cursor: pointer" onclick="javascript:changeTabEPS(1);">EPS tương đương</a></li>
        <li><a id="lstab2EPS" style="cursor: pointer" onclick="javascript:changeTabEPS(2);">P/E tương đương</a></li>
    </ul>
    <div style="clear:both"></div>
     <div id='divData1EPS'>
    <div id='divData1EPSInner'>
        <table width="100%" border="0" cellspacing="0" cellpadding="0">
            <tr>
                <th class="col1" align="center">Mã</th>
                <th class="col1" align="center">Sàn</th>
                <th class="col2">EPS</th>
                <th class="col3">Giá</th>
                <th class="col4">P/E</th>
                <th class="col5" width="75">Vốn hóa TT (Tỷ đồng)</th>
            </tr>
            
                    <tr class="even">
                        <td  align="center"><a title='C&#244;ng ty Cổ phần X&#226;y dựng 47' href='http://s.cafef.vn/hose/C47-cong-ty-co-phan-xay-dung-47.chn'>C47</a></td>
                        <td  align="center">HSX</td>
                        <td>2.6</td>
                        <td>11.9</td>
                        <td>4.7</td>
                        <td>233.2</td>
                    </tr>
                
                    <tr class="odd">
                        <td  align="center"><a title='C&#244;ng ty cổ phần Cảng C&#225;t L&#225;i' href='http://s.cafef.vn/hose/CLL-cong-ty-co-phan-cang-cat-lai.chn'>CLL</a></td>
                        <td align="center">HSX</td>
                        <td>2.6</td>
                        <td>28.0</td>
                        <td>10.7</td>
                        <td>1,013.2</td>
                    </tr>
                
                    <tr class="even">
                        <td  align="center"><a title='C&#244;ng ty cổ phần Thế giới số' href='http://s.cafef.vn/hose/DGW-cong-ty-co-phan-the-gioi-so.chn'>DGW</a></td>
                        <td  align="center">HSX</td>
                        <td>2.7</td>
                        <td>25.3</td>
                        <td>9.2</td>
                        <td>921.6</td>
                    </tr>
                
                    <tr class="odd">
                        <td  align="center"><a title='C&#244;ng ty Cổ phần Vận tải v&#224; Xếp dỡ Hải An' href='http://s.cafef.vn/hose/HAH-cong-ty-co-phan-van-tai-va-xep-do-hai-an.chn'>HAH</a></td>
                        <td align="center">HSX</td>
                        <td>2.7</td>
                        <td>14.3</td>
                        <td>5.2</td>
                        <td>672.5</td>
                    </tr>
                
                    <tr class="even">
                        <td  align="center"><a title='C&#244;ng ty Cổ phần Dịch vụ &#212; t&#244; H&#224;ng Xanh' href='http://s.cafef.vn/hose/HAX-cong-ty-co-phan-dich-vu-o-to-hang-xanh.chn'>HAX</a></td>
                        <td  align="center">HSX</td>
                        <td>2.8</td>
                        <td>16.3</td>
                        <td>5.8</td>
                        <td>590.0</td>
                    </tr>
                
                    <tr class="odd">
                        <td  align="center"><a title='C&#244;ng ty Cổ phần Chứng kho&#225;n Th&#224;nh phố Hồ Ch&#237; Minh' href='http://s.cafef.vn/hose/HCM-cong-ty-co-phan-chung-khoan-thanh-pho-ho-chi-minh.chn'>HCM</a></td>
                        <td align="center">HSX</td>
                        <td>2.6</td>
                        <td>24.5</td>
                        <td>9.3</td>
                        <td>8,766.5</td>
                    </tr>
                
                    <tr class="even">
                        <td  align="center"><a title='Tổng C&#244;ng ty cổ phần Thiết bị điện Việt Nam' href='http://s.cafef.vn/hose/GEX-tong-cong-ty-co-phan-thiet-bi-dien-viet-nam.chn'>GEX</a></td>
                        <td  align="center">HSX</td>
                        <td>2.6</td>
                        <td>22.7</td>
                        <td>8.8</td>
                        <td>9,391.5</td>
                    </tr>
                
                    <tr class="odd">
                        <td  align="center"><a title='C&#244;ng ty cổ phần Đầu tư Hải Ph&#225;t' href='http://s.cafef.vn/hose/HPX-cong-ty-co-phan-dau-tu-hai-phat.chn'>HPX</a></td>
                        <td align="center">HSX</td>
                        <td>2.6</td>
                        <td>26.2</td>
                        <td>10.1</td>
                        <td>4,719.9</td>
                    </tr>
                
                    <tr class="even">
                        <td  align="center"><a title='C&#244;ng ty Cổ phần Đầu tư ph&#225;t triển hạ tầng IDICO' href='http://s.cafef.vn/hose/HTI-cong-ty-co-phan-dau-tu-phat-trien-ha-tang-idico.chn'>HTI</a></td>
                        <td  align="center">HSX</td>
                        <td>2.7</td>
                        <td>11.5</td>
                        <td>4.2</td>
                        <td>296.9</td>
                    </tr>
                
                    <tr class="odd">
                        <td  align="center"><a title='C&#244;ng ty Cổ phần Đầu tư v&#224; C&#244;ng nghệ HVC' href='http://s.cafef.vn/hose/HVH-cong-ty-co-phan-dau-tu-va-cong-nghe-hvc.chn'>HVH</a></td>
                        <td align="center">HSX</td>
                        <td>2.5</td>
                        <td>17.8</td>
                        <td>7.0</td>
                        <td>452.0</td>
                    </tr>
                
        </table>
    </div>
    <div id="ctl00_ContentPlaceHolder1_SameEPS_PE_paging" class="paging"><a style='padding-left=5px' href='javascript:ViewPageNextPreviousEPS(-1)'>&lt;</a>&nbsp;<a id='aSameEPS1' href='javascript:ViewPageSameEPSByIndex(1);' class='current'>1</a>&nbsp;<a id='aSameEPS2' href='javascript:ViewPageSameEPSByIndex(2);'>2</a>&nbsp;<a id='aSameEPS3' href='javascript:ViewPageSameEPSByIndex(3);'>3</a>&nbsp;<a id='aSameEPS4' href='javascript:ViewPageSameEPSByIndex(4);'>4</a>&nbsp;<a id='aSameEPS5' href='javascript:ViewPageSameEPSByIndex(5);'>5</a>&nbsp;<a id='aSameEPS6' href='javascript:ViewPageSameEPSByIndex(6);'>6</a>&nbsp;<a id='aSameEPS7' href='javascript:ViewPageSameEPSByIndex(7);'>7</a>&nbsp;<a id='aSameEPS8' href='javascript:ViewPageSameEPSByIndex(8);'>8</a>&nbsp;<a href='javascript:ViewPageNextPreviousEPS(1)'>&gt;</a>&nbsp;</div><div class="pagingnote" id="pagingnoteeps">Trang 1/8 (Tổng số  78 công ty)</div>
        <div class="epse-note" id="eps_pe_notes">(EPS +/-0.5)</div><input type="hidden" id="txtIdxSameEPS" value="1" enableviewstate=false /></div>
    <div id="divData2EPS">
     <div id='divData2EPSInner'></div>
        <div class="" id="pagingPE"></div>
        <div class="epse-note" id="eps_pe_notespe">(PE +/-1.0)</div>
        <input type="hidden" id="txtIdxSamePE" value="1" enableviewstate=false />
    </div>
 </div>
 <script language="javascript" type="text/javascript">
var TotalPagePE = '8';
var TotalItemPE = '78';
var strPE = ""; var strPEPaging = ""; var pagingPE = document.getElementById("pagingPE"); var divData1EPS = document.getElementById("divData1EPS"); var divData2EPS = document.getElementById("divData2EPS"); var tab1EPS = document.getElementById("lstab1EPS"); var tab2EPS = document.getElementById("lstab2EPS"); divData2EPS.style.display = "none"; document.getElementById('txtIdxSameEPS').value = 1; document.getElementById('txtIdxSamePE').value = 1;
var symbol = 'A32';
$(document).ready(function(e) { changeTabEPS(1); });
</script>


                        <!-- end -->
                        <!--tag cloud for cp-->
                        
                        <!--end-->
                        
                    </div>
                    <!-- //sidebar -->
                    
                    <div class="totop" style="text-align: center; border: none; color: #999;"><b>(*) Lưu ý:</b> Dữ liệu được CafeF tổng hợp từ các nguồn đáng tin cậy, có giá trị tham khảo với các nhà đầu tư.<br />
                        Tuy nhiên, chúng tôi không chịu trách nhiệm trước mọi rủi ro nào do sử dụng các dữ liệu này.</div>
                    <div class="totop"><a href="#">[ Về đầu trang ]</a></div>
                    <div class="doitac clearfix">
                        
                    </div>
                    <div style="background-color: #fff; padding-top: 10px; margin: 0 10px">
                        
<div id="footerv22">

<div class="adv_full_bottom clearfix">
</div>
    <div class="clearfix"></div>

    <div class="menucategory menuheader clearfix" id="menu_wrap">
        <div class="wp1040 relative">
            <ul>
                <li class="bt_home active"><a href="//cafef.vn" title="Trang chủ" class="sprite"></a></li>
                <li class="li_left"><a href="//cafef.vn/thoi-su.chn" title="THỜI SỰ">THỜI SỰ</a></li>
                <li><a href="//cafef.vn/thi-truong-chung-khoan.chn" title="CHỨNG KHOÁN">CHỨNG KHOÁN</a></li>
                <li><a href="/cafef.vn/bat-dong-san.chn" title="BẤT ĐỘNG SẢN">BẤT ĐỘNG SẢN</a></li>
                <li><a href="//cafef.vn/doanh-nghiep.chn" title="DOANH NGHIỆP">DOANH NGHIỆP</a></li>
                <li><a href="//cafef.vn/tai-chinh-ngan-hang.chn" title="NGÂN HÀNG">NGÂN HÀNG</a></li>
                <li><a href="//cafef.vn/tai-chinh-quoc-te.chn" title="TÀI CHÍNH QUỐC TẾ">TÀI CHÍNH QUỐC TẾ</a></li>
                <li><a href="//cafef.vn/vi-mo-dau-tu.chn" title="VĨ MÔ">VĨ MÔ</a></li>
                <li><a href="//cafef.vn/song.chn" title="SỐNG">SỐNG</a></li>
                <li><a href="//cafef.vn/hang-hoa-nguyen-lieu.chn" title="HÀNG HÓA">HÀNG HÓA</a></li>               
                <li class="menucategory_right"><a href="http://s.cafef.vn/top/ceo.chn" title="Top 200">Top 200</a></li>
                <li class="menucategory_right"><a href="http://s.cafef.vn/du-lieu.chn" title="Dữ liệu">Dữ liệu</a></li>
            </ul>
        </div>
    </div>

<div class="clearfix"></div>
<div class="wrap clearfix">
    <div class="ft-cp" style="border: none; width: 360px; padding-left: 0;">
        <a href="http://www.vccorp.vn" title="Công ty Cổ phần truyền thông Việt Nam - VCCorp" rel="nofollow" target="_blank"><img align="left" width="130px" style="padding-right: 10px;" src="http://adi.vcmedia.vn/logo/runbyvcc.e.png" alt="VCCorp" border="0"/></a> 
        <strong>Copyright 2007</strong> - Công ty Cổ phần VCCorp.<br />
        Tầng 17, 19, 20, 21 Tòa nhà Center Building - Hapulico Complex<br />
        Số 1 Nguyễn Huy Tưởng, Thanh Xuân, Hà Nội.<br />
        Giấy phép thiết lập trang thông tin điện tử tổng hợp trên internet số 1084/GP-STTTT do Sở Thông tin và Truyền thông Hà Nội cấp ngày 16 tháng 4 năm 2014.
    </div>
    <div class="ft-info" style="width:350px;">
        Ban biên tập CafeF, Tầng 21, tòa nhà Center Building.<br />
        Số 1 Nguyễn Huy Tưởng, Thanh Xuân, Hà Nội.<br />
        Điện thoại: 04 7309 5555 <span>Máy lẻ 41292</span>. Fax: 04-39744082<br />
        Email: <a href="mailto:info@cafef.vn">info@cafef.vn</a><br />
        Ghi rõ nguồn "CafeF" khi phát hành lại thông tin từ kênh thông tin này.<br />&nbsp;        
    </div>
    <div class="ft-qc" style="padding-left: 20px; border-left: solid 1px #ccc; width: 200px;">
        <b>Liên hệ quảng cáo: </b>Ms. Hương<br />
        Mobile: 0934 252 233<br />
        Email: <a href="mailto:doanhnghiep@admicro.vn">doanhnghiep@admicro.vn</a><br />
        <b>Hỗ trợ &amp; CSKH :</b> Ms. Thơm<br />
        Mobile: 01268 269 779<br />&nbsp;
    </div>
</div>
<input name="ctl00$ContentPlaceHolder1$UcFooter1$hdIP" type="hidden" id="ctl00_ContentPlaceHolder1_UcFooter1_hdIP" />

<script type="text/javascript">    
    GetDate();
    setTimeout("GetDate()",10000);
    function popupPolicy() {
        modalWindow.windowId = "policyModal";
        modalWindow.width = 610;
        modalWindow.height = 470;
        modalWindow.force = null;
        modalWindow.content = "<div style='background-color:#fff;padding: 20px;border: solid 1px green;'><p style='font-weight:bold;margin-bottom: 10px;font-size: 130%;'>Thỏa thuận chia sẻ nội dung</p> <p style='line-height: 20px;font-size: 110%;'>Các nội dung do VCCorp đại diện kinh doanh có thể được các báo, trang tin điện tử, website sử dụng đăng tải lại (trên nguyên tắc trích dẫn nguyên văn nội dung, ghi nguồn, tên tác giả đầy đủ), trừ khi có yêu cầu hoặc thỏa thuận riêng khác bằng văn bản giữa 2 bên. Điều đó cũng được hiểu là VCCorp cũng có quyền sử dụng đăng tải lại các nội dung từ các báo, trang tin điện tử, website có quan hệ chia sẻ theo nguyên tắc này.</p></div>";
        modalWindow.open();
    }
</script>
<a href="javascript:void(0);" style="float:left;padding-top:5px;color:#c00;" onclick="popupPolicy();">Thỏa thuận chia sẻ nội dung</a>
<style type="text/css">#seoshare li {float:right; margin-right:5px; text-transform:uppercase;}#seoshare li span{height: 21px; width:5px; background: url(http://cafef3.vcmedia.vn/v2/images/seoshare.png) top left no-repeat scroll; float:left;}#seoshare li span.right {background-position: -5px 0;float:right;} #seoshare a{background:url(http://cafef3.vcmedia.vn/v2/images/seoshare.png) repeat-x 0px -21px scroll; padding: 4px 3px 0 3px; float:left; height:17px; overflow:hidden; color:#000; font-size: 11px; font-weight:bold; text-align: center;}</style>
<div id="seoshare"><ul><li><span class="left"></span><span class="right"></span><a href="http://cafebiz.vn/" title="CafeBiz - Thông tin kinh doanh - Doanh nhân" target="_blank">CafeBiz.vn</a></li><li><span class="left"></span><span class="right"></span><a href="http://sannhac.com/home" title="SànNhạc.com" target="_blank">SanNhac.com</a></li><li><span class="left"></span><span class="right"></span><a href="http://afamily.vn/" title="Kênh thông tin dành cho phụ nữ, đẹp, gia đình, giải trí, thời trang" target="_blank">aFamily.vn</a></li><li><span class="left"></span><span class="right"></span><a href="http://f319.com/home" title="Thị trường chứng khoán - F319.com" target="_blank">F319</a></li></ul></div>
    </div>
                    </div>
                </div>
                <div class="bobottom">
                </div>
                
            </div>
        </div>
        <!-- //Pagewrap background -->
    </div>
    <style type="text/css">
        .close-window {
            top: -15px;
            right: -15px;
        }
    </style>
    <script type="text/javascript">
        function popupsend() {
            modalWindow.windowId = "policyModal";
            modalWindow.width = 610;
            modalWindow.height = 470;
            modalWindow.force = null;
            modalWindow.content = '<div class="comment clearfix" style="background-color:#fff;padding:20px;border: solid 1px green;"><div class="cm-form"><h3>Gửi thông tin về lỗi dữ liệu</h3><div class="cmfcontent"><label for="hotem">Họ tên</label><input type="text" class="formtext" id="hoten" /><label for="email">Email</label><input type="text" class="formtext" id="email" /><input class="formsubmit" style="cursor:pointer;" onclick="return SendError();" title="GỬI" type="button" value="GỬI" /></div></div><div class="cm-form" id="divNoiDung2" style="padding-top:22px"><label for="noidung">Nội dung</label><textarea cols="" class="formtextarea" id="noidung" style="height: 150px; width:340px"></textarea></div>';
            modalWindow.open();
        }
    </script>
    <link href="http://cafef3.vcmedia.vn/v2/styles/comment.css" media="screen" rel="stylesheet" type="text/css" />
    <script type="text/javascript">
        function Validate() {
            var ht = document.getElementById('hoten');
            var email = document.getElementById('email');
            var noidung = document.getElementById('noidung');
            if (ht.value == "" || email.value == "") {
                alert("Bạn chưa nhập đầy đủ thông tin!");
                return false;
            }
            if (noidung != null) {
                if (noidung.value == "") {
                    alert("Bạn chưa nhập đầy đủ thông tin!");
                    return false;
                }
            }
            return true;
        }
        function SendError() {
            var ht = document.getElementById('hoten');
            var email = document.getElementById('email');
            var noidung = document.getElementById('noidung');
            var symb = 'A32'
        if (Validate()) {
            $.ajax({
                type: "GET",
                url: "/Ajax/FinancialIndex/SendFB.aspx?error=true&symbol=" + symb,
                data: "ht=" + encodeURIComponent(ht.value) + "&email=" + email.value + "&noidung=" + encodeURIComponent(noidung.value),
                success: function (msg) {
                    alert("Cảm ơn bạn đã báo lỗi. Chúng tôi sẽ cố gắng khắc phục trong thời gian sớm nhất!");
                    modalWindow.close();
                }
            });
            return true;
        }
        else {
            return false;
        }
    }
    </script>

        </div>
    </form>
    <script type="text/javascript">
        MenuActive(1000);
    </script>
    <script src="http://cafef3.vcmedia.vn/v2/scripts/footer.js" type="text/javascript"></script>
 <script src="http://cafef3.vcmedia.vn/reporting/slog.js"></script>
    <script type="text/javascript">
        LogValue();
        var _laq = _laq || [];
        _laq.push(['_setApp', 'LA-56744888-16']);
        _laq.push(['_trackPageview']);
        (function () {
            var la = document.createElement('script'); la.type = 'text/javascript'; la.async = true;
            la.src = "http://logscafef.channelvn.net/scripts/log.js";
            var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(la, s);
        })();
    </script>

	<script>
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-PMC2DK4');
</script>

    <script type="text/javascript">        
        $(document).ready(function () {
            $("#back-top").hide();
            $(function () {
                $(window).scroll(function () {
                    if ($(this).scrollTop() > 500) {
                        $('#scroll_top').fadeIn();
                    } else {
                        $('#scroll_top').fadeOut();
                    }
                    if ($(this).scrollTop() > 210) {
                        $('#menuv3').css("position", "fixed").css("top", "0").css("box-shadow", "0 2px 4px #333");
                    }
                    else {
                        $('#menuv3').css("position", "relative").css("box-shadow", "none");
                    }
                });
                $('#scroll_top').click(function () {
                    $('body,html').animate({ scrollTop: 0 }, 800);
                    return false;
                });
            });
        });
    </script>
    <style type="text/css">
        #scroll_top {
            background: url("http://cafef3.vcmedia.vn/v2/images/scrollTop.png") no-repeat scroll 0 0 transparent;
            cursor: pointer;
            display: none;
            height: 46px;
            opacity: 0.5;
            position: fixed;
            right: 10px;
            top: 80%;
            width: 46px;
            z-index: 999;
        }

            #scroll_top:hover {
                opacity: 1;
            }

        .Top3LinksForGoogleSearchResult {
            height: 0px;
            overflow: hidden;
        }
    </style>
    <div id="scroll_top" style="display: none;"></div>
    <div id="ctl00_Top3LinksForGoogleSearchResult" class="Top3LinksForGoogleSearchResult"><li itemscope="" itemtype="http://schema.org/Event"><time itemprop="startDate" datetime="9/29/2019 5:58:05 PM"></time><time itemprop="endDate" datetime="">9/29/2019 5:58:05 PM</time><a href="/ceo/CEO_55601/ong-vu-xuan-tao.chn" itemprop="url"><strong itemprop="name">Chủ tịch HĐQT </strong></a><span itemprop="performers"></span><p itemprop="location" itemscope="" itemtype="http://schema.org/Place"><span itemprop="name"><a href="/ceo/CEO_55601/ong-vu-xuan-tao.chn" itemprop="url">Ông Vũ Xuân Tạo</a></span></p></li><li itemscope="" itemtype="http://schema.org/Event"><time itemprop="startDate" datetime="9/28/2019 5:58:05 PM"></time><time itemprop="endDate" datetime="">9/28/2019 5:58:05 PM</time><a href="/Lich-su-giao-dich-A32-1.chn" itemprop="url"><strong itemprop="name">Giá cổ phiếu </strong></a><span itemprop="performers"></span><p itemprop="location" itemscope="" itemtype="http://schema.org/Place"><span itemprop="name"><a href="/Lich-su-giao-dich-A32-1.chn" itemprop="url">27</a></span></p></li><li itemscope="" itemtype="http://schema.org/Event"><time itemprop="startDate" datetime="9/28/2019 5:58:05 PM"></time><time itemprop="endDate" datetime="">9/28/2019 5:58:05 PM</time><a href="/Lich-su-giao-dich-A32-1.chn" itemprop="url"><strong itemprop="name">Giá cổ phiếu </strong></a><span itemprop="performers"></span><p itemprop="location" itemscope="" itemtype="http://schema.org/Place"><span itemprop="name"><a href="/Lich-su-giao-dich-A32-1.chn" itemprop="url">27</a></span></p></li><li itemscope="" itemtype="http://schema.org/Event"><time itemprop="startDate" datetime="9/27/2019 5:58:05 PM"></time><time itemprop="endDate" datetime="">9/27/2019 5:58:05 PM</time><a href="/bao-cao-tai-chinh/A32/IncSta/2018/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-32.chn" itemprop="url"><strong itemprop="name">Kết quả KD: Giá vốn hàng bán</strong></a><span itemprop="performers"></span><p itemprop="location" itemscope="" itemtype="http://schema.org/Place"><span itemprop="name"><a href="/bao-cao-tai-chinh/A32/IncSta/2018/0/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-32.chn" itemprop="url">583,746,959,157 VNĐ (năm 2018)</a></span></p></li></div>
    
</body>
</html>"""

def tryToGetThumbnailByBrief(soup):
    try:
        thumbnailUrl = soup.find("img", {"class": "img"})['src']
        return thumbnailUrl
    except Exception as e:
        return ""

def tryToGetThumbnailByAvatar(soup):
    try:
        avatar = soup.find_all("div", class_="avartar")[0]
        print(avatar.img.get('src'))
    except Exception as e:
        return ""

def getCompanyThumbnail(soup):
    thumbnailUrlBrief = tryToGetThumbnailByBrief(soup)
    thumbnailUrlAvatar = tryToGetThumbnailByAvatar(soup)

    if thumbnailUrlBrief != "":
        return thumbnailUrlBrief 
    elif thumbnailUrlAvatar != "":
        return thumbnailUrlAvatar
    else:
        return ""

soup = BeautifulSoup(response, "html.parser")
thumbnailUrl = getCompanyThumbnail(soup)