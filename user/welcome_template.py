def template(name):
    return '''<!DOCTYPE html>
<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<title>Welcome to CoFinder</title>
		<style>
			/* -------------------------------------
          GLOBAL RESETS
      ------------------------------------- */

			/*All the styling goes here*/

			img {
				border: none;
				-ms-interpolation-mode: bicubic;
				max-width: 100%;
			}

			body {
				background-color: #f6f6f6;
				font-family: Helvetica, sans-serif;
				-webkit-font-smoothing: antialiased;
				font-size: 14px;
				line-height: 1.4;
				margin: 0;
				padding: 0;
				-ms-text-size-adjust: 100%;
				-webkit-text-size-adjust: 100%;
			}

			table {
				border-collapse: separate;
				mso-table-lspace: 0pt;
				mso-table-rspace: 0pt;
				width: 100%;
			}
			table td {
				font-family: sans-serif;
				font-size: 14px;
				vertical-align: top;
			}

			/* -------------------------------------
          BODY & CONTAINER
      ------------------------------------- */

			.body {
				background-color: #f6f6f6;
				width: 100%;
			}

			/* Set a max-width, and make it display as block so it will automatically stretch to that width, but will also shrink down on a phone or something */
			.container {
				display: block;
				margin: 0 auto !important;
				/* makes it centered */
				max-width: 580px;
				padding: 10px;
				width: 580px;
			}

			/* This should also be a block element, so that it will fill 100% of the .container */
			.content {
				box-sizing: border-box;
				display: block;
				margin: 0 auto;
				max-width: 580px;
				padding: 10px;
			}

			/* -------------------------------------
          HEADER, FOOTER, MAIN
      ------------------------------------- */
			.main {
				background: #ffffff;
				border-radius: 3px;
				width: 100%;
			}

			.wrapper {
				box-sizing: border-box;
				padding: 32px;
			}

			.content-block {
				padding-bottom: 10px;
				padding-top: 10px;
			}

			.footer {
				clear: both;
				margin-top: 10px;
				text-align: center;
				width: 100%;
			}
			.footer td,
			.footer p,
			.footer span,
			.footer a {
				color: #999999;
				font-size: 12px;
				text-align: center;
			}

			/* -------------------------------------
          TYPOGRAPHY
      ------------------------------------- */
			h1,
			h2,
			h3,
			h4 {
				color: #000000;
				font-weight: 400;
				line-height: 1.4;
				margin: 0;
				margin-bottom: 30px;
			}

			h1 {
				font-size: 35px;
				font-weight: 300;
				line-height: 1.15;
			}

			p,
			ul,
			ol {
				color: #444444;
				font-size: 16px;
				font-weight: normal;
				margin: 0;
				margin-bottom: 15px;
			}
			p li,
			ul li,
			ol li {
				list-style-position: inside;
				margin-left: 5px;
			}

			a {
				color: #298442;
				text-decoration: none;
				font-weight: 600;
			}

			/* -------------------------------------
          BUTTONS
      ------------------------------------- */
			.btn {
				box-sizing: border-box;
				width: 100%;
			}
			.btn > tbody > tr > td {
				padding-bottom: 15px;
			}
			.btn table {
				width: auto;
			}
			.btn table td {
				background-color: #ffffff;
				border-radius: 5px;
				text-align: center;
			}
			.btn a {
				background-color: #ffffff;
				border: solid 1px #298442;
				border-radius: 2px;
				box-sizing: border-box;
				color: #298442;
				cursor: pointer;
				display: inline-block;
				font-size: 14px;
				font-weight: bold;
				margin: 0;
				padding: 12px 25px;
				text-decoration: none;
				text-transform: capitalize;
				letter-spacing: 0.5px;
			}

			.btn-primary table td {
				background-color: #298442;
			}

			.btn-primary a {
				background-color: #298442;
				border-color: #298442;
				color: #ffffff;
			}

			/* -------------------------------------
          OTHER STYLES THAT MIGHT BE USEFUL
      ------------------------------------- */
			.last {
				margin-bottom: 0;
			}

			.first {
				margin-top: 0;
			}

			.align-center {
				text-align: center;
			}

			.align-right {
				text-align: right;
			}

			.align-left {
				text-align: left;
			}

			.clear {
				clear: both;
			}

			.mt0 {
				margin-top: 0;
			}

			.mb0 {
				margin-bottom: 0;
			}

			.text-sm {
				font-size: 13px;
			}

			.preheader {
				color: transparent;
				display: none;
				height: 0;
				max-height: 0;
				max-width: 0;
				opacity: 0;
				overflow: hidden;
				mso-hide: all;
				visibility: hidden;
				width: 0;
			}

			.powered-by a {
				text-decoration: none;
			}

			hr {
				border: 0;
				border-bottom: 1px solid #f6f6f6;
				margin: 20px 0;
			}

			/* -------------------------------------
          RESPONSIVE AND MOBILE FRIENDLY STYLES
      ------------------------------------- */
			@media only screen and (max-width: 620px) {
				table.body h1 {
					font-size: 28px !important;
					margin-bottom: 10px !important;
				}
				table.body p,
				table.body ul,
				table.body ol,
				table.body td,
				table.body span,
				table.body a {
					font-size: 16px !important;
				}
				table.body .wrapper,
				table.body .article {
					padding: 10px !important;
				}
				table.body .content {
					padding: 0 !important;
				}
				table.body .container {
					padding: 0 !important;
					width: 100% !important;
				}
				table.body .main {
					border-left-width: 0 !important;
					border-radius: 0 !important;
					border-right-width: 0 !important;
				}
				table.body .btn table {
					width: 100% !important;
				}
				table.body .btn a {
					width: 100% !important;
				}
				table.body .img-responsive {
					height: auto !important;
					max-width: 100% !important;
					width: auto !important;
				}
			}

			/* -------------------------------------
          PRESERVE THESE STYLES IN THE HEAD
      ------------------------------------- */
			@media all {
				.ExternalClass {
					width: 100%;
				}
				.ExternalClass,
				.ExternalClass p,
				.ExternalClass span,
				.ExternalClass font,
				.ExternalClass td,
				.ExternalClass div {
					line-height: 100%;
				}
				.apple-link a {
					color: inherit !important;
					font-family: inherit !important;
					font-size: inherit !important;
					font-weight: inherit !important;
					line-height: inherit !important;
					text-decoration: none !important;
				}
				#MessageViewBody a {
					color: inherit;
					text-decoration: none;
					font-size: inherit;
					font-family: inherit;
					font-weight: inherit;
					line-height: inherit;
				}
				.btn-primary table td:hover {
					background-color: #34495e !important;
				}
				.btn-primary a:hover {
					background-color: #34495e !important;
					border-color: #34495e !important;
				}
			}
		</style>
	</head>
	<body>
		<span class="preheader"
			>We are excited to have you onboard!</span
		>
		<table
			role="presentation"
			border="0"
			cellpadding="0"
			cellspacing="0"
			class="body"
		>
			<tr>
				<td>&nbsp;</td>
				<td class="container">
					<div class="content">
						<!-- START CENTERED WHITE CONTAINER -->
						<table role="presentation" class="main">
							<!-- START MAIN CONTENT AREA -->
							<tr>
								<td class="wrapper">
									<table
										role="presentation"
										border="0"
										cellpadding="0"
										cellspacing="0"
									>
										<tr>
											<td>
												<a
													href="https://cofinder.ca"
													target="_blank"
													><img
														src="https://cofinder.ca/assets/branding-2175b10e.png"
														width="40px"
												/></a>
												<br />
												<br />
												<h1>
													Welcome to CoFinder!<br />Let's get
													you upto speed.
												</h1>
                                                <br />
												<p>Hi ''' + name + ''',</p>
												<p>We are excited to have you onboard.</p>
												<p>
													With CoFinder, you can make your UFV
													schedule, check calendar, see your
													week at a glance and so much more.
												</p>
												<br />
												<table
													role="presentation"
													border="0"
													cellpadding="0"
													cellspacing="0"
													class="btn btn-primary"
												>
													<tbody>
														<tr>
															<td align="left">
																<table
																	role="presentation"
																	border="0"
																	cellpadding="0"
																	cellspacing="0"
																>
																	<tbody>
																		<tr>
																			<td>
																				<a
																					href="https://cofinder.ca"
																					target="_blank"
																					>MAKE
																					YOUR
																					SCHEDULE</a
																				>
																			</td>
																		</tr>
																	</tbody>
																</table>
															</td>
														</tr>
													</tbody>
												</table>
												<hr />
												<p class="text-sm">
													We may send emails in future if they
													be beneficial for you or to convey any
													policy changes. We will never send
													marketing emails.
												</p>
												<br />
												<div class="align-center">
													CoFinder 2023.
													<a
														href="mailto:admin@cofinder.ca"
														target="_blank"
														>Contact Us</a
													>
												</div>
											</td>
										</tr>
									</table>
								</td>
							</tr>

							<!-- END MAIN CONTENT AREA -->
						</table>
						<!-- END CENTERED WHITE CONTAINER -->
					</div>
				</td>
				<td>&nbsp;</td>
			</tr>
		</table>
	</body>
</html>
'''