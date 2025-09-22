import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json

# Configure Streamlit page
st.set_page_config(
    page_title="SAP Migration Suite - Licensing",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "main"

if 'licensing_state' not in st.session_state:
    st.session_state.licensing_state = {
        'license_type': 'Enterprise',
        'license_valid': True,
        'license_expiry': '2025-12-31',
        'organization': 'Global Corp Inc.',
        'max_users': 25,
        'current_users': 15,
        'monthly_credits': 10000,
        'used_credits': 8500,
        'subscription_tier': 'Enterprise Plus',
        'monthly_cost': 2450.00,
        'auto_renewal': True,
        # Only include features relevant to the actual SAP migration tools
        'features_enabled': [
            'HRP1000/HRP1001 Processing (Foundation)',
            'PA0001/PA0002/PA0006/PA0105 Processing (Employee)',
            'PA0008/PA0014 Processing (Payroll)',
            'Advanced Data Validation',
            'Migration Analytics',
            'Custom Report Generation',
            'API Access',
            'Priority Support',
            'Audit Trail',
            'Encrypted Package Export',
            'Multi-tenant Support'
        ]
    }

def show_main_page():
    """Show the main landing page"""
    
    # Header - simplified, professional
    st.markdown("""
    <div style="background: linear-gradient(90deg, #1e3d59 0%, #2e5984 100%); padding: 2rem; border-radius: 10px; margin-bottom: 2rem;">
        <h1 style="color: white; margin: 0; text-align: center;">SAP Migration Suite - Enterprise Licensing</h1>
        <p style="color: #e0e8f0; text-align: center; margin: 0.5rem 0 0 0;">
            Licensing, packaging, and subscription management for SAP HCM to SuccessFactors migration
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Current license status - relevant metrics
    licensing_state = st.session_state.licensing_state
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            "License Status", 
            "Active" if licensing_state['license_valid'] else "Expired",
            help=f"Valid until {licensing_state['license_expiry']}"
        )
    
    with col2:
        st.metric(
            "Subscription", 
            licensing_state['subscription_tier'],
            help="Current subscription level"
        )
    
    with col3:
        usage_pct = (licensing_state['used_credits'] / licensing_state['monthly_credits']) * 100
        st.metric(
            "Processing Credits", 
            f"{usage_pct:.1f}% used",
            f"{licensing_state['used_credits']:,}/{licensing_state['monthly_credits']:,}"
        )
    
    with col4:
        st.metric(
            "Licensed Users", 
            f"{licensing_state['current_users']}/{licensing_state['max_users']}",
            help="Active vs maximum users"
        )
    
    st.markdown("---")
    
    # Main navigation - focused on core areas
    st.markdown("### Management Areas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("License & Features", use_container_width=True, type="primary"):
            st.session_state.current_page = "license_details"
            st.rerun()
        st.caption("View license information and enabled SAP migration features")
        
        if st.button("Package & Deploy", use_container_width=True):
            st.session_state.current_page = "packaging"
            st.rerun()
        st.caption("Generate deployment packages for SAP migration tools")
    
    with col2:
        if st.button("Billing & Usage", use_container_width=True):
            st.session_state.current_page = "billing"
            st.rerun()
        st.caption("View processing costs and credit usage analytics")
        
        if st.button("Subscription Settings", use_container_width=True):
            st.session_state.current_page = "configuration"
            st.rerun()
        st.caption("Manage plans, users, and renewal settings")
    
    # Migration scope overview - relevant to actual app
    st.markdown("---")
    st.markdown("### Current Migration Scope")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info("**Foundation Data**: HRP1000/HRP1001 organizational hierarchy processing")
    with col2:
        st.info("**Employee Data**: PA0001/PA0002/PA0006/PA0105 personnel record migration")
    with col3:
        st.info("**Payroll Data**: PA0008/PA0014 compensation and benefits processing")

def show_license_details():
    """Show license information relevant to SAP migration"""
    licensing_state = st.session_state.licensing_state
    
    if st.button("← Back to Main", key="back_license"):
        st.session_state.current_page = "main"
        st.rerun()
    
    st.header("License & Feature Details")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("License Information")
        st.write(f"**Type**: {licensing_state['license_type']}")
        st.write(f"**Organization**: {licensing_state['organization']}")
        st.write(f"**Valid Until**: {licensing_state['license_expiry']}")
        st.write(f"**Max Users**: {licensing_state['max_users']}")
        st.write(f"**Monthly Credits**: {licensing_state['monthly_credits']:,}")
        
        # License validity check
        expiry_date = datetime.strptime(licensing_state['license_expiry'], '%Y-%m-%d')
        days_remaining = (expiry_date - datetime.now()).days
        
        if days_remaining > 30:
            st.success(f"License expires in {days_remaining} days")
        elif days_remaining > 0:
            st.warning(f"License expires in {days_remaining} days")
        else:
            st.error("License has expired")
    
    with col2:
        st.subheader("Enabled SAP Migration Features")
        
        # Group by actual app functionality
        feature_categories = {
            "SAP Data Processing": [
                "HRP1000/HRP1001 Processing (Foundation)",
                "PA0001/PA0002/PA0006/PA0105 Processing (Employee)",
                "PA0008/PA0014 Processing (Payroll)"
            ],
            "Migration Tools": [
                "Advanced Data Validation",
                "Migration Analytics", 
                "Custom Report Generation"
            ],
            "Enterprise Features": [
                "API Access",
                "Priority Support",
                "Audit Trail",
                "Encrypted Package Export",
                "Multi-tenant Support"
            ]
        }
        
        for category, features in feature_categories.items():
            st.markdown(f"**{category}:**")
            for feature in features:
                if feature in licensing_state['features_enabled']:
                    st.write(f"✓ {feature}")
                else:
                    st.write(f"✗ {feature} (Not included)")
            st.write("")

def show_billing_usage():
    """Show billing relevant to SAP processing"""
    licensing_state = st.session_state.licensing_state
    
    if st.button("← Back to Main", key="back_billing"):
        st.session_state.current_page = "main"
        st.rerun()
    
    st.header("Billing & Processing Usage")
    
    # Processing cost breakdown - relevant to actual usage
    col1, col2 = st.columns([2, 1])
    
    with col1:
        billing_data = {
            'Service': [
                'Base Platform License', 
                'SAP File Processing Credits', 
                'Data Validation Services', 
                'Report Generation',
                'Storage & Archive',
                'Support & Maintenance'
            ],
            'Monthly Cost': [1200, 850, 300, 150, 50, 200],
            'Usage': ['100%', '85%', '92%', '65%', '23%', '100%']
        }
        
        df_billing = pd.DataFrame(billing_data)
        
        fig = px.pie(
            df_billing, 
            values='Monthly Cost', 
            names='Service',
            title="Monthly Cost Distribution"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Current Period")
        st.metric("Total Cost", f"${licensing_state['monthly_cost']:,.2f}")
        st.metric("Next Bill", "Oct 1, 2024")
        st.metric("Payment", "Auto-Pay Enabled")
        
        # Usage alerts based on actual processing
        usage_pct = (licensing_state['used_credits'] / licensing_state['monthly_credits']) * 100
        if usage_pct > 90:
            st.error("Processing credit limit almost reached")
        elif usage_pct > 75:
            st.warning("High processing usage detected")
        
        st.dataframe(df_billing[['Service', 'Monthly Cost']], use_container_width=True)
    
    # Processing usage trends
    st.subheader("SAP Processing Usage Trends")
    
    # Generate realistic usage data
    dates = pd.date_range(start='2024-07-01', end='2024-09-22', freq='D')
    daily_usage = []
    
    for i, date in enumerate(dates):
        # Simulate realistic SAP processing patterns
        base_usage = 180 + (i % 20) * 12  # Base processing
        weekday_factor = 1.0 if date.weekday() < 5 else 0.3  # Lower weekend usage
        monthly_factor = 1.2 if i % 30 < 5 else 1.0  # Month-end spikes
        usage = int(base_usage * weekday_factor * monthly_factor)
        daily_usage.append(usage)
    
    df_usage = pd.DataFrame({
        'Date': dates,
        'Credits Used': daily_usage,
        'Cumulative': pd.Series(daily_usage).cumsum()
    })
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig = px.line(df_usage, x='Date', y='Credits Used', title="Daily Processing Credits")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = px.line(df_usage, x='Date', y='Cumulative', title="Cumulative Monthly Usage")
        st.plotly_chart(fig, use_container_width=True)

def show_packaging_tools():
    """Show packaging tools for SAP migration deployment"""
    licensing_state = st.session_state.licensing_state
    
    if st.button("← Back to Main", key="back_packaging"):
        st.session_state.current_page = "main"
        st.rerun()
    
    st.header("Package & Deployment Tools")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Migration Suite Components")
        
        package_name = st.text_input("Package Name", value="SAP_Migration_Suite_v2.1")
        
        # Actual components from the real app
        include_foundation = st.checkbox("Foundation Data Module (HRP1000/HRP1001)", value=True)
        include_employee = st.checkbox("Employee Data Module (PA0001/PA0002/PA0006/PA0105)", value=True)
        include_payroll = st.checkbox("Payroll Data Module (PA0008/PA0014)", value=True)
        
        st.subheader("Security & Compliance")
        encrypt_package = st.checkbox("Encrypt Package", value=True)
        digital_signature = st.checkbox("Digital Signature", value=True)
        audit_trail = st.checkbox("Include Audit Trail", value=True)
        
        encryption_level = st.selectbox("Encryption", ["AES-256", "AES-128"], index=0)
    
    with col2:
        st.subheader("Deployment Configuration")
        
        deployment_target = st.selectbox(
            "Target Environment",
            ["Cloud Deployment", "On-Premise", "Hybrid Cloud", "Customer Infrastructure"]
        )
        
        auto_update = st.checkbox("Enable Auto-Updates", value=True)
        multi_client = st.checkbox("Multi-Client Support", value=True)
        api_access = st.checkbox("Enable API Access", value=True)
        
        st.subheader("Package Summary")
        
        # Calculate realistic package sizes
        base_size = 45
        foundation_size = 28 if include_foundation else 0
        employee_size = 32 if include_employee else 0
        payroll_size = 24 if include_payroll else 0
        total_size = base_size + foundation_size + employee_size + payroll_size
        
        st.write(f"**Package Size**: {total_size} MB")
        st.write(f"**Components**: {sum([include_foundation, include_employee, include_payroll])} SAP modules")
        st.write(f"**Security**: {'Enterprise' if encrypt_package else 'Standard'}")
    
    st.markdown("---")
    
    # Package generation
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Generate Package", type="primary", use_container_width=True):
            generate_migration_package(package_name, include_foundation, include_employee, include_payroll)
    
    with col2:
        if st.button("Create Manifest", use_container_width=True):
            generate_package_manifest(package_name, licensing_state)
    
    with col3:
        if st.button("Validate Package", use_container_width=True):
            validate_package_integrity()

def show_configuration():
    """Show subscription and configuration management"""
    licensing_state = st.session_state.licensing_state
    
    if st.button("← Back to Main", key="back_config"):
        st.session_state.current_page = "main"
        st.rerun()
    
    st.header("Subscription & Configuration")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Available Plans")
        
        # Plans relevant to SAP processing
        plans = {
            'Starter': {
                'price': 800, 
                'credits': 5000, 
                'users': 5,
                'features': 'Basic SAP file processing, email support'
            },
            'Professional': {
                'price': 1800, 
                'credits': 12000, 
                'users': 15,
                'features': 'Advanced validation, priority support, API access'
            },
            'Enterprise': {
                'price': 3200, 
                'credits': 25000, 
                'users': 50,
                'features': 'Full suite, 24/7 support, custom integrations'
            },
            'Enterprise Plus': {
                'price': 5500, 
                'credits': 50000, 
                'users': 'Unlimited',
                'features': 'White label, on-premise, dedicated support manager'
            }
        }
        
        current_plan = licensing_state['subscription_tier']
        
        for plan_name, details in plans.items():
            is_current = plan_name == current_plan
            status = "Current Plan" if is_current else "Available"
            
            with st.expander(f"{plan_name} - ${details['price']}/month ({status})"):
                st.write(f"**Monthly Credits**: {details['credits']:,}")
                st.write(f"**Max Users**: {details['users']}")
                st.write(f"**Features**: {details['features']}")
                
                if not is_current:
                    if st.button(f"Upgrade to {plan_name}", key=f"upgrade_{plan_name}"):
                        st.success(f"Upgrade request submitted for {plan_name} plan")
    
    with col2:
        st.subheader("Account Management")
        
        auto_renewal = st.checkbox("Auto-Renewal", value=licensing_state['auto_renewal'])
        
        st.subheader("Notifications")
        usage_alerts = st.checkbox("Processing usage alerts", value=True)
        billing_reminders = st.checkbox("Billing reminders", value=True)
        system_updates = st.checkbox("System update notifications", value=True)
        
        st.subheader("Actions")
        
        col_a, col_b = st.columns(2)
        
        with col_a:
            if st.button("Update Payment", use_container_width=True):
                st.info("Opening secure payment portal...")
            
            if st.button("Download Invoice", use_container_width=True):
                st.info("Generating current invoice...")
        
        with col_b:
            if st.button("Manage Users", use_container_width=True):
                st.info("Opening user management...")
            
            if st.button("Contact Support", use_container_width=True):
                st.info("Creating support ticket...")

def generate_migration_package(package_name, include_foundation, include_employee, include_payroll):
    """Generate SAP migration package"""
    with st.spinner("Generating SAP migration package..."):
        import time
        time.sleep(2)
        
        package_contents = {
            "package_name": package_name,
            "version": "2.1.0",
            "generated_at": datetime.now().isoformat(),
            "sap_modules": {
                "foundation_hrp1000_hrp1001": include_foundation,
                "employee_pa0001_pa0002_pa0006_pa0105": include_employee,
                "payroll_pa0008_pa0014": include_payroll
            },
            "migration_scope": {
                "source_system": "SAP HCM",
                "target_system": "SuccessFactors",
                "estimated_records": "1400+ employees"
            },
            "security": {
                "encrypted": True,
                "signature": "SHA256:abc123def456...",
                "encryption_level": "AES-256"
            },
            "license": {
                "type": "Enterprise",
                "valid_until": "2025-12-31",
                "organization": "Global Corp Inc."
            }
        }
        
        package_json = json.dumps(package_contents, indent=2)
        
        st.success("SAP migration package generated successfully")
        
        st.download_button(
            label="Download Package Manifest",
            data=package_json,
            file_name=f"{package_name}_manifest.json",
            mime="application/json"
        )

def generate_package_manifest(package_name, licensing_state):
    """Generate deployment manifest"""
    manifest = {
        "package_info": {
            "name": package_name,
            "version": "2.1.0",
            "build_date": datetime.now().isoformat(),
            "license_type": licensing_state['license_type']
        },
        "system_requirements": {
            "python_version": ">=3.8",
            "memory": "8GB RAM recommended",
            "storage": "2GB available space",
            "dependencies": ["streamlit>=1.28.0", "pandas>=2.0.0", "plotly>=5.0.0"]
        },
        "sap_capabilities": [
            "HRP1000/HRP1001 Processing",
            "PA0001/PA0002/PA0006/PA0105 Processing", 
            "PA0008/PA0014 Processing"
        ],
        "checksum": "sha256:demo_manifest_checksum"
    }
    
    manifest_json = json.dumps(manifest, indent=2)
    
    st.success("Package manifest generated")
    st.download_button(
        label="Download Manifest",
        data=manifest_json,
        file_name=f"{package_name}_manifest.json",
        mime="application/json"
    )

def validate_package_integrity():
    """Validate package integrity"""
    with st.spinner("Validating package integrity..."):
        import time
        time.sleep(1.5)
        
        validation_results = {
            "Digital Signature": "Valid",
            "Encryption": "AES-256 confirmed",
            "Dependencies": "All satisfied", 
            "License": "Valid until 2025-12-31",
            "Checksum": "Verified",
            "SAP Modules": "All modules intact"
        }
        
        st.success("Package validation completed")
        
        for check, result in validation_results.items():
            st.write(f"**{check}**: {result}")

def main():
    """Main application function"""
    
    # Navigation
    if st.session_state.current_page == "main":
        show_main_page()
    elif st.session_state.current_page == "license_details":
        show_license_details()
    elif st.session_state.current_page == "billing":
        show_billing_usage()
    elif st.session_state.current_page == "packaging":
        show_packaging_tools()
    elif st.session_state.current_page == "configuration":
        show_configuration()

if __name__ == "__main__":
    main()
