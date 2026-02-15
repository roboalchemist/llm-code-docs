# Getting started

**Source:** [https://developer.wordpress.org/apis/abilities-api/getting-started/](https://developer.wordpress.org/apis/abilities-api/getting-started/)



# Getting started



↑Back to top



The Abilities API was added to WordPress inversion 6.9.


For backwards compatibility, you can check if theWP_Abilityclass is available.


```
if ( ! class_exists( 'WP_Ability' ) ) {
	// E.g. add an admin notice about the missing dependency.
	add_action(
		'admin_notices',
		static function () {
			wp_admin_notice(
				esc_html__( 'This plugin requires the Abilities API, which is only available in WordPress 6.9 or newer. Please update your WordPress version to use this plugin.', 'textdomain' ),
				'error'
			);
		}
	);

	return;
}
```


## Basic Usage Example


The below example is for a plugin implementation, but it could also be adapted for a theme’sfunctions.php


```
<?php
// 1. Register the ability when the Abilities API is initialized.
// Using `wp_abilities_api_init` ensures the API is fully loaded.
add_action( 'wp_abilities_api_init', 'wporg_register_abilities' );
/**
 * Register custom abilities.
 *
 * @return void
 */
function wporg_register_abilities() {
	wp_register_ability(
		'wporg/get-site-title',
		array(
			'label'               => __( 'Get Site Title', 'textdomain' ),
			'description'         => __( 'Retrieves the title of the current WordPress site.', 'textdomain' ),
			'output_schema'       => array(
				'type'        => 'string',
				'description' => 'The site title.',
			),
			'execute_callback'    => 'wporg_get_site_title',
			'permission_callback' => '__return_true', // Everyone can access this.
			'meta'                => array(
				'category'     => 'site-info',
				'show_in_rest' => true, // Optional: expose via REST API.
			),
		)
	);
}
// 2. Define a callback function for your ability.
/**
 * Callback to get the site title.
 *
 * @return string
 */
function wporg_get_site_title(): string {
	return get_bloginfo( 'name' );
}


// 3. Later, you can retrieve and execute the ability.
add_action( 'admin_init', 'wporg_use_ability' );
/**
 * Use the registered ability.
 *
 * @return void
 */
function wporg_use_ability() {
	$ability = wp_get_ability( 'wporg/get-site-title' );
	if ( ! $ability ) {
		// Ability not found.
		return;
	}

	$site_title = $ability->execute();
	if ( is_wp_error( $site_title ) ) {
		// Handle execution error.
		error_log( 'Execution error: ' . $site_title->get_error_message() );
		return;
	}

	// `$site_title` now holds the result of `get_bloginfo( 'name' )`.
	echo 'Site Title: ' . esc_html( $site_title );
}
```





First published


December 3, 2025






[PreviousAbilities APIPrevious: Abilities API](https://developer.wordpress.org/apis/abilities-api/)
[NextHooksNext: Hooks](https://developer.wordpress.org/apis/abilities-api/hooks/)


